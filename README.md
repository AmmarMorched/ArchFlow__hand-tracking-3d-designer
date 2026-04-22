# ArchFlow__hand-tracking-3d-designer

ArchFlow is a real-time hand tracking system that uses a webcam to control 3D objects inside Unity.  
It allows natural interaction using hand gestures (movement + pinch detection) to manipulate a virtual object in space.

---

## Current Version (MVP)

This version implements a working prototype with:

- Real-time hand tracking using webcam
- Finger position detection (index finger)
- Pinch gesture detection (thumb + index distance)
- Data streaming from Python to Unity via UDP
- Smooth 3D cube control in Unity
- Basic pinch interaction (grab effect)

---

## How It Works

### 1. Python (Computer Vision Layer)
- Uses MediaPipe to detect hand landmarks
- Extracts:
  - Index finger position (X, Y)
  - Pinch state (distance between thumb and index)
- Applies smoothing to reduce noise
- Sends data via UDP socket

### 2. Unity (3D Interaction Layer)
- Receives real-time data from Python
- Maps 2D coordinates into 3D space
- Moves a cube smoothly using interpolation
- Applies visual feedback when pinch is active

---

## Tech Stack

### Python Side:
- OpenCV
- MediaPipe
- Socket programming (UDP)

### Unity Side:
- Unity Engine
- C# scripting
- Real-time UDP communication

---

## Features Implemented

- ✔ Hand tracking via webcam
- ✔ Real-time coordinate streaming
- ✔ Pinch gesture detection
- ✔ Smooth object movement
- ✔ Basic 3D interaction in Unity
- ✔ Visual feedback (scale change on grab)

---

## Data Flow

Webcam
↓
MediaPipe (hand tracking)
↓
Python processing + smoothing
↓
UDP socket stream
↓
Unity receiver script
↓
3D object manipulation

---

## project structure

ArchFlow/
│
├── python/
│ ├── main.py # Hand tracking + UDP sender
│
├── unity/
│ ├── Assets/
│ │ ├── Scripts/
│ │ │ ├── HandTrackingReceiver.cs
│ │ │ ├── CubeController.cs
│
├── README.md

---


---

## ⚙️ How to Run

## 1. Python Side
```bash
pip install opencv-python mediapipe
python main.py
```

## 2. Unity side
1. Open Unity project
2. Press Play
3. Ensure scene has:
   - Main Camera
   - Cube object
   - Receiver + Controller scripts attached

---

### Current limitation: 

- Depth (Z-axis) is approximated (not true 3D hand tracking)
- Some jitter due to webcam noise
- Only single object manipulation supported
- No UI for object creation yet

---

### Next Steps (Roadmap)

Wait and see 


### 👨‍💻 Author

- Morched Ammar
- Embedded Systems / AI / Computer Vision Enthusiast