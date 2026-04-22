using UnityEngine;

public class CubeController : MonoBehaviour
{
    public HandTrackingReceiver receiver;
    public float smoothSpeed = 10f;

    private Vector3 velocity = Vector3.zero;

    void Update()
    {
        if (receiver == null) return;

        // Normalize input
        float x = receiver.x / 640f;
        float y = receiver.y / 480f;

        // Flip X for natural movement
        x = 1f - x;

        // 3D mapping
        float worldX = (x - 0.5f) * 8f;
        float worldY = 1f + (1f - y) * 5f;   // height control
        float worldZ = (1f - y) * 8f;        // depth control

        Vector3 target = new Vector3(worldX, worldY, worldZ);

        // Smooth movement (ALWAYS, not only pinch)
        transform.position = Vector3.Lerp(
            transform.position,
            target,
            12f * Time.deltaTime
        );

        // Optional: pinch effect (visual only for now)
        if (receiver.pinch)
        {
            transform.localScale = Vector3.Lerp(
                transform.localScale,
                Vector3.one * 1.2f,
                Time.deltaTime * 10f
            );
        }
        else
        {
            transform.localScale = Vector3.Lerp(
                transform.localScale,
                Vector3.one,
                Time.deltaTime * 10f
            );
        }
    }
}
