import java.net.*;
import java.io.*;

public class test_DHCP_Server {
    public static void main(String[] args) throws IOException{
        server s = new server();
        s.recieveMessage();
    }
}

public class server {
    final static int SERVER_PORT_NUMBER=67;
    final static int CLIENT_PORT_NUMBER=68;
    private static boolean running;
    private static  DatagramSocket server;
    private static byte[] buffer;

    public server() throws IOException{
        server = new DatagramSocket(SERVER_PORT_NUMBER);
    }
    public void recieveMessage()throws IOException{
        running = true;
        while(running){
            buffer = new byte[256];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            server.receive(packet);
            String response = new String(packet.getData());
            System.out.println("Response data : "+response);
            if (response.equals("end")) {
                running = false;
                continue;
            }
        }
        server.close();
    }
}

