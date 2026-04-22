using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class HandTrackingReceiver : MonoBehaviour
{
    UdpClient client;
    public int port = 5052;

    public float x;
    public float y;
    public bool pinch;

    void Start()
    {
        client = new UdpClient(port);
        client.BeginReceive(new AsyncCallback(ReceiveData), null);
    }

    void ReceiveData(IAsyncResult result)
    {
        IPEndPoint remoteEP = new IPEndPoint(IPAddress.Any, port);
        byte[] data = client.EndReceive(result, ref remoteEP);

        string message = Encoding.UTF8.GetString(data);
        string[] values = message.Split(',');

        if (values.Length == 3)
        {
            x = float.Parse(values[0]);
            y = float.Parse(values[1]);
            pinch = values[2] == "1";
        }

        client.BeginReceive(new AsyncCallback(ReceiveData), null);
    }
}
