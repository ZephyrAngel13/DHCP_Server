import java.net.*;
import java.io.*;

public class client{
    public static void main(String[] args) throws IOException{
        DatagramSocket client = new DatagramSocket();
        InetAddress address = InetAddress.getByName("localhost");
        String string = "Success!";
        byte[] buffer = string.getBytes();
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length,address,4160);
        client.send(packet);
        client.close();
    }
}