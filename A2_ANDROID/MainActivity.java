package com.example.rohan.autofill;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;


public class MainActivity extends Activity implements android.view.View.OnClickListener{
    Button btnSave;
    EditText First,Last,Phone,Email,Pwd;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnSave = (Button) findViewById(R.id.button);
        First   = (EditText) findViewById(R.id.editText);
        Last   = (EditText) findViewById(R.id.editText2);
        Phone   = (EditText) findViewById(R.id.editText3);
        Email   = (EditText) findViewById(R.id.editText4);
        Pwd   = (EditText) findViewById(R.id.editText5);

        btnSave.setOnClickListener(this);
        SharedPreferences pref = getSharedPreferences("ActivityPREF", Context.MODE_PRIVATE);
        if(pref.getBoolean("activity_executed", false)){
            Intent intent = new Intent(this, Next.class);
            startActivity(intent);
            finish();
        } else {
            SharedPreferences.Editor ed = pref.edit();
            ed.putBoolean("activity_executed", true);
            ed.commit();
        }


    }
    public void onClick(View view) {
        if (view == findViewById(R.id.button)) {
            try {

                File myFile = new File("/sdcard/profile.txt");
                myFile.createNewFile();
                FileOutputStream fOut = new FileOutputStream(myFile);
                OutputStreamWriter myOutWriter = new OutputStreamWriter(fOut);
                myOutWriter.append(  First.getText()+"\n");
                myOutWriter.append(  Last.getText()+"\n");
                myOutWriter.append(  Phone.getText()+"\n");
                myOutWriter.append(  Email.getText()+"\n");
                myOutWriter.append(  Pwd.getText()+"\n");
                myOutWriter.close();
                fOut.close();
                Toast.makeText(getBaseContext(), "Profile saved successfully ", Toast.LENGTH_SHORT).show();
                Intent intent1 = new Intent(this,Thanks.class);
                startActivity(intent1);
                finish();
            } catch (Exception e) {
                Toast.makeText(getBaseContext(), e.getMessage(), Toast.LENGTH_SHORT).show();
            }

        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
