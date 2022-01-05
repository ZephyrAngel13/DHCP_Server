import java.net.*;
import java.io.*;

public class server {
    final static int SERVER_PORT_NUMBER=67;
    final static int CLIENT_PORT_NUMBER=68;
    public static void main(String[] args) throws IOException{
        DatagramSocket server = new DatagramSocket(SERVER_PORT_NUMBER);
        byte[] buffer = new byte[256];
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
        server.receive(packet);
        String response = new String(packet.getData());
        System.out.println("Response data : "+response);
        server.close();
    }
    
}