package com.example.cmpe273.EAttendance;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class chooseActivity extends AppCompatActivity {

    EditText choiceR, choiceC;
    Button signUpButton, checkinButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_choose);
        setUpUI();


        signUpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i("TAG", "Inside Choose");
                final Context context = getApplicationContext();
                String text = "Signing Up ";
                Toast.makeText(getApplicationContext(), text, Toast.LENGTH_SHORT).show();
                Intent nextScreen = new Intent(chooseActivity.this, RegisterActivity.class);
                //discoverableIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
                startActivity(nextScreen);

            }

        });
        checkinButton.setOnClickListener(new View.OnClickListener(){
                    public void onClick(View v) {
                        Log.i("TAG", "Inside Choose");
                        final Context context = getApplicationContext();
                        String text = "Checking in ";
                        Toast.makeText(getApplicationContext(), text, Toast.LENGTH_SHORT).show();
                        Intent nextScreen2 = new Intent(chooseActivity.this, LoginActivity.class);
                        //discoverableIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
                        startActivity(nextScreen2);
                    }

        });

    }

    private void setUpUI(){

        signUpButton = (Button)findViewById(R.id.regButton);
        checkinButton = (Button)findViewById(R.id.checkInButton);

    }
}
