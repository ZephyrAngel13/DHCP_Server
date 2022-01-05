import java.net.*;
import java.io.*;

public class test_DHCP_Client {
    public static void main(String[] args) throws IOException{
        client s = new client();
        s.sendMessage("Mama");
        s.sendMessage("are");
        s.sendMessage("mere");
        s.sendMessage("end");
        s.close();
    }
}

public class client{
    final static int SERVER_PORT_NUMBER=67;
    final static int CLIENT_PORT_NUMBER=68;
    private static InetAddress address;
    private static  DatagramSocket client;
    private static byte[] buffer;

    public client() throws IOException{
        client = new DatagramSocket();
        address = InetAddress.getByName("localhost");
    }
    public void sendMessage(String message)throws IOException{
        buffer = message.getBytes();
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length,address,SERVER_PORT_NUMBER);
        client.send(packet);
        
    }
    public void close(){
        client.close();
    }
}