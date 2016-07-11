package com.example.cmpe273.EAttendance;

import android.bluetooth.BluetoothAdapter;
import android.content.Context;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.IOException;
import java.util.UUID;
import android.content.Intent;


public class RegisterActivity extends AppCompatActivity {


    private static final UUID SERVICE_UID = UUID.fromString("94f39d29-7d6d-437d-973b-fba39e49d4ff");
    EditText ename, eid, epass;
    Button signUpButton;
    private BluetoothAdapter mBluetoothAdapter;

    String getReply;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        //TODO: Might be an exception
        getSupportActionBar().hide();

        setUpUI();

        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        if (!mBluetoothAdapter.isEnabled()) {
            Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivityForResult(enableBtIntent, 1);
        }
        Intent discoverableIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
        discoverableIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
        startActivity(discoverableIntent);



        signUpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i("TAG", "Inside Sign Up");


                signUpButton.setEnabled(false);
                final Context context = getApplicationContext();
                String text = "Attempting to Register";

                Toast.makeText(context, text, Toast.LENGTH_SHORT).show();
                final String msg = readJSONString();

                AsyncTask<Void, String, String> connectAsyncTask = new AsyncTask<Void, String, String>() {
                    @Override
                    protected String doInBackground(Void... params)
                    {
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
                        boolean checkF = false;

                        char c=s.charAt(0);
                        Log.i("print",String.valueOf(c));
                        /*int a=Integer.parseInt(s);
                        Log.i("intg",String.valueOf(a));*/
                        if (c=='1')
                        {
                            checkF=true;
                            Toast.makeText(context, "Registration Successful", Toast.LENGTH_SHORT).show();
                        }
                        else if(c=='3')
                        {
                            Toast.makeText(context, "Student not found - Invalid record", Toast.LENGTH_SHORT).show();
                        }
                        else if(c=='2')

                        {
                            checkF=true;
                            Toast.makeText(context, "Already Registered", Toast.LENGTH_SHORT).show();
                        }
                        else
                        {
                            Toast.makeText(context, "Network failure - Please try again", Toast.LENGTH_SHORT).show();
                        }

                        signUpButton.setEnabled(true);
                        if(checkF==true) {
                            Intent nextScreen = new Intent(RegisterActivity.this, chooseActivity.class);
                            //discoverableIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
                            startActivity(nextScreen);
                        }

                    }
                };

                connectAsyncTask.executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, null);
            }
        });

    }

    public void onSignUpFailed() {
        Toast.makeText(getBaseContext(), "Login failed", Toast.LENGTH_LONG).show();

        signUpButton.setEnabled(true);
    }

    private String readJSONString() {
        String[] keyName = {"eid", "ename", "epass"};

        EditText[] editTexts = {eid, ename, epass};
        JSONObject jsonObj = new JSONObject();
        try {
            //jsonObj.put("bid", myaddress);
            for (int i = 0; i < keyName.length; i++) {
                jsonObj.put(keyName[i], editTexts[i].getText());
            }

        } catch (JSONException ex) {
            ex.printStackTrace();
        }
        return jsonObj.toString();
    }

    private void setUpUI() {
        ename = (EditText)findViewById(R.id.ename);
        eid = (EditText)findViewById(R.id.eid);
        epass = (EditText)findViewById(R.id.epass);
        signUpButton = (Button)findViewById(R.id.btnSignUp);

    }



}
