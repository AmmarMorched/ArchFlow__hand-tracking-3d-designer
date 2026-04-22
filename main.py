import cv2
import mediapipe as mp
import math
import socket

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 5052)

cap = cv2.VideoCapture(0)

def distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

# --- smoothing state ---
smooth_x, smooth_y = 0, 0
alpha = 0.2  # lower = smoother

while True:
    success, img = cap.read()
    if not success:
        continue

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    pinch = False

    if results.multi_hand_landmarks:

        # 👉 ONLY use first hand (important for stability)
        handLms = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

        # landmarks
        thumb_tip = handLms.landmark[4]
        index_tip = handLms.landmark[8]

        # pinch detection
        dist = distance(thumb_tip, index_tip)
        pinch = dist < 0.05

        # target position (index finger)
        h, w, _ = img.shape
        cx = int(index_tip.x * w)
        cy = int(index_tip.y * h)

        # --- smoothing (IMPORTANT FIX) ---
        smooth_x = int(alpha * cx + (1 - alpha) * smooth_x)
        smooth_y = int(alpha * cy + (1 - alpha) * smooth_y)

        # draw debug point
        cv2.circle(img, (smooth_x, smooth_y), 10, (255, 0, 0), cv2.FILLED)

        # send clean data
        data = f"{smooth_x},{smooth_y},{int(pinch)}"
        sock.sendto(data.encode(), server_address)

    # UI text
    if pinch:
        cv2.putText(img, "GRABBING", (50, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
    else:
        cv2.putText(img, "NOT GRABBING", (50, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
