package com.example.cmpe273.EAttendance;
import android.bluetooth.BluetoothAdapter;
import android.content.Context;
import android.content.Intent;
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

/**
 * A login screen that offers login via email/password.
 */
public class LoginActivity extends AppCompatActivity  {
    private BluetoothAdapter mBluetoothAdapter;
    private static final UUID SERVICE_UID = UUID.fromString("94f39d29-7d6d-437d-973b-fba39e49d4aa");

    // UI references.

    private EditText lpass, lid;
    Button log_in_button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        //TODO: Might be an exception
        getSupportActionBar().hide();
        setUpUI();

        // Set up the login form.

        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        if (!mBluetoothAdapter.isEnabled()) {
            Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivityForResult(enableBtIntent, 1);
        }
        Intent discoverableIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);
        discoverableIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
        startActivity(discoverableIntent);



        log_in_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i("TAG", "Inside Sign Up");


                log_in_button.setEnabled(false);
                final Context context = getApplicationContext();
                String text = "Attempting to Log in";

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
                        boolean checkF=false;
                        char c=s.charAt(0);

                        if(c=='1') {
                            checkF=true;
                            Toast.makeText(context, "Login Successful", Toast.LENGTH_SHORT).show();
                        }
                        else if(c=='3') {
                            Toast.makeText(context, "Student not found - Invalid record", Toast.LENGTH_SHORT).show();
                        }
                        else if(c=='2') {
                            Toast.makeText(context, "Authentication failure", Toast.LENGTH_SHORT).show();
                        }
                        else {
                            Toast.makeText(context, "Network failure, Please try again", Toast.LENGTH_SHORT).show();
                        }
                        log_in_button.setEnabled(true);

                        if(checkF==true) {
                            Intent nextScreen = new Intent(LoginActivity.this, checkinActivity.class);
                            //discoverableIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
                            Log.i("pp", lid.getText().toString());
                            Bundle bun = new Bundle();
                            bun.putString("sid", lid.getText().toString());
                            nextScreen.putExtras(bun);

                            startActivity(nextScreen);
                        }


                    }
                };

                connectAsyncTask.executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, null);
            }
        });

    }

    private void setUpUI() {

        lid = (EditText)findViewById(R.id.lid);
        lpass = (EditText)findViewById(R.id.lpass);
        log_in_button = (Button)findViewById(R.id.login_in_button);

    }

    private String readJSONString() {
        String[] keyName = {"lid", "lpass"};

        EditText[] editTexts = {lid, lpass};
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


}

