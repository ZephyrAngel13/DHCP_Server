import java.net.*;
import java.io.*;

public class client{
    final static int CLIENT_PORT_NUMBER=68;
    public static void main(String[] args) throws IOException{
        DatagramSocket client = new DatagramSocket();
        InetAddress address = InetAddress.getByName("localhost");
        String string = "Success!";
        byte[] buffer = string.getBytes();
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length,address,CLIENT_PORT_NUMBER);
        client.send(packet);
        client.close();
    }
}