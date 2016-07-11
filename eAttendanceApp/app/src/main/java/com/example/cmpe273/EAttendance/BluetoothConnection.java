package com.example.cmpe273.EAttendance;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.util.Log;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.UUID;

class BluetoothConnection extends Thread {
    public BluetoothSocket mmSocket;
    // private final InputStream mmInStream;
    public OutputStream mmOutStream;
    public InputStream mmInStream;
    public byte[] buffer = new byte[1024];
    String addr = "B8:27:EB:55:17:87";  //"88:53:2E:43:32:B6";  nexus // "B8:27:EB:55:17:87" rpi

    // Unique UUID for this application, you may use different

    public BluetoothConnection(final BluetoothAdapter mbluetoothAdapter, UUID uuid) {

        BluetoothSocket tmp = null;
        final BluetoothDevice device = mbluetoothAdapter.getRemoteDevice(addr);

        // Get a BluetoothSocket for a connection with the given BluetoothDevice
        try {
            tmp = device.createRfcommSocketToServiceRecord(uuid);
        } catch (IOException e) {
            e.printStackTrace();
        }
        mmSocket = tmp;

        //now make the socket connection in separate thread to avoid FC
        Thread connectionThread  = new Thread(new Runnable() {

            @Override
            public void run() {
                // Always cancel discovery because it will slow down a connection
                mbluetoothAdapter.cancelDiscovery();

                // Make a connection to the BluetoothSocket
                try {
                    // This is a blocking call and will only return on a
                    // successful connection or an exception
                    mmSocket.connect();



                } catch (IOException e) {
                    //connection to device failed so close the socket
                    try {
                        mmSocket.close();
                    } catch (IOException e2) {
                        e2.printStackTrace();
                    }
                }


            }
        });

        connectionThread.start();

        try {
            connectionThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }


    }

    public void read() {

        // Keep listening to the InputStream while connected
        while (true) {
            try {
                //read the data from socket stream
                mmInStream = mmSocket.getInputStream();
                mmInStream.read(buffer);
                Log.e("msg", (buffer.toString()));
                // Send the obtained bytes to the UI Activity
            } catch (IOException e) {
                //an exception here marks connection loss
                //send message to UI Activity
                break;
            }
        }
    }

    public void write(byte[] buff) {
        try {
            //write the data to socket stream
            mmOutStream = mmSocket.getOutputStream();
            mmOutStream.write(buff);
        } catch (IOException e) {
            System.out.println(e.toString());
        }
    }

    public void cancel() {
        try {
            mmSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
