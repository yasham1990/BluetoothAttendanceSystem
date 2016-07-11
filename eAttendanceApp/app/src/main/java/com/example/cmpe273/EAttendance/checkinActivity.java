package com.example.cmpe273.EAttendance;

import android.bluetooth.BluetoothAdapter;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;

import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.IOException;
import java.util.UUID;

public class checkinActivity extends AppCompatActivity {

    private BluetoothAdapter mBluetoothAdapter;
    private static final UUID SERVICE_UID = UUID.fromString("94f39d29-7d6d-437d-973b-fba39e49d4bb");

    Button checkInButton;
    JSONObject jsonObj;
    Spinner dropdown;
    String value;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_checkin);
        setUpUI();
        Bundle extrab = getIntent().getExtras();
        if (extrab != null) {
            value = extrab.getString("sid");
        }


        dropdown = (Spinner) findViewById(R.id.classes);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.class_name, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        dropdown.setAdapter(adapter);

        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        if (!mBluetoothAdapter.isEnabled()) {
            Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivityForResult(enableBtIntent, 1);
        }
        Intent discoverableIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
        discoverableIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
        startActivity(discoverableIntent);

        checkInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkInButton.setEnabled(false);

                //Log.i("dropdown", ss);
                final Context context = getApplicationContext();
                String text = "Checking in..";

                Toast.makeText(context, text, Toast.LENGTH_SHORT).show();
                final String msg = readJSONString();
                AsyncTask<Void, String, String> connectAsyncTask = new AsyncTask<Void, String, String>() {
                    @Override
                    protected String doInBackground(Void... params) {
                        BluetoothConnection conn = new BluetoothConnection(mBluetoothAdapter, SERVICE_UID);
                        try {
                            // Log.i("message_value", String(msg.getBytes()));
                            conn.write(msg.getBytes("utf-8"));
                            this.publishProgress("Sending your Information");
                            conn.read();
                            String server_msg = new String(conn.buffer);
                            return server_msg;
                            //this.publishProgress(server_msg);
                        } catch (IOException e) {

                            e.printStackTrace();
                        }
                        return null;
                    }

                    @Override
                    protected void onProgressUpdate(String... values) {
                        super.onProgressUpdate(values);
                        Toast.makeText(context, values[0], Toast.LENGTH_SHORT).show();
                    }

                    @Override
                    protected void onPostExecute(String s) {
                        super.onPostExecute(s);
                        if(!(s.equals("Attendance marked")) || s.equals("Attendance not marked,timeover") || s.equals("Invalid checkin"))
                        {
                            s=s;
                        }
                        else if(s.contains("constraint"))
                        {
                            s="Already checked in";
                        }
                        else
                        {
                            s="Network failure, Please try again";
                        }
                        Toast.makeText(context, s, Toast.LENGTH_SHORT).show();
                        setContentView(R.layout.activity_checkin);
                        TextView textView = (TextView) findViewById(R.id.aText);
                        textView.setText(s);
                        //  Toast.makeText(context, "Attendance Marked", Toast.LENGTH_SHORT).show();
                        checkInButton.setEnabled(true);
                        //finish();

                    }
                };

                connectAsyncTask.executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, null);
            }
        });

    }

    private String readJSONString() {
        String ss = dropdown.getSelectedItem().toString();
        Log.i("newval", value);
        jsonObj = new JSONObject();

        try {
            //jsonObj.put("bid", myaddress);

            jsonObj.put("course", ss);
            jsonObj.put("cid", value);
        } catch (JSONException ex) {
            ex.printStackTrace();
        }
        return jsonObj.toString();
    }

    private void setUpUI() {

        checkInButton = (Button) findViewById(R.id.checkInButton);

    }

}
