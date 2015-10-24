package com.example.rohan.autofill;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;


public class AutoFilling extends Activity {

    String first = "";
    String last = "";
    String phone = "";
    String email = "";
    String password = "";
    String data= "";
    String full=  "";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_auto_filling);
        try {
            File myFile = new File("/sdcard/profile.txt");
            FileInputStream fIn = new FileInputStream(myFile);
            BufferedReader myReader = new BufferedReader(new InputStreamReader(fIn));

            int i  = 0;
            while (( data= myReader.readLine()) != null) {
                if (i == 0)
                    first = data;
                else if (i == 1)
                    last = data;
                else if (i == 2)
                    phone = data;
                else if (i == 3)
                    email = data;
                else if (i == 4)
                    password = data;
                i++;
            }
            full = first +" "+last;
            myReader.close();
            Toast.makeText(getBaseContext(), "Done reading ", Toast.LENGTH_SHORT).show();
        } catch (Exception e) {
            Toast.makeText(getBaseContext(), e.getMessage(), Toast.LENGTH_SHORT).show();
        }
        System.out.println(first);
        System.out.println(last);
        System.out.println(phone);
        System.out.println(email);
        System.out.println(password);

        Intent i = getIntent();
        String url =i.getDataString();
        //String url ="https://accounts.google.com/signup?hl=en-GB";
        WebView myWebView = (WebView) findViewById(R.id.webview);
        WebSettings webSettings = myWebView.getSettings();
        myWebView.getSettings().setDomStorageEnabled(true);
        myWebView.loadUrl(url);
        webSettings.setJavaScriptEnabled(true);
        myWebView.setWebViewClient(new WebViewClient() {
            public void onPageFinished(WebView view, String url) {

                view.loadUrl("javascript:var x = document.getElementById('FirstName').value = '"+first+"';");
                view.loadUrl("javascript:var x = document.getElementById('LastName').value = '"+last+"';");
                view.loadUrl("javascript:var x = document.getElementById('GmailAddress').value = '"+email+"';");
                view.loadUrl("javascript:var x = document.getElementById('Passwd').value = '"+password+"';");
                view.loadUrl("javascript:var x = document.getElementById('PasswdAgain').value = '"+password+"';");
                view.loadUrl("javascript:var x = document.getElementById('j_password').value = '"+password+"';");
                view.loadUrl("javascript:var x = document.getElementById('j_confpassword').value = '"+password+"';");
                view.loadUrl("javascript:var x = document.getElementById('RecoveryPhoneNumber').value = '"+phone+"';");
                view.loadUrl("javascript:var x = document.getElementById('j_number').value = '"+phone+"';");
                view.loadUrl("javascript:var x = document.getElementById('RecoveryEmailAddress').value = '"+email+"';");
                view.loadUrl("javascript:var x = document.getElementById('Email').value = '"+email+"';");
                view.loadUrl("javascript:var x = document.getElementById('j_username_new').value = '"+email+"';");
                view.loadUrl("javascript:var x = document.getElementById('oauth_signup_client_fullname').value = '"+full+"';");
                view.loadUrl("javascript:var x = document.getElementById('A1ef5e4c859f79a98605340e6306f2cb79c39d4c9').value = '"+phone+"';");
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_auto_filling, menu);
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
