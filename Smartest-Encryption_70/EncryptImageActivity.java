package me.theoduino.imageencryptor;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.support.v4.view.accessibility.AccessibilityNodeInfoCompat;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Random;

public class EncryptImageActivity extends ActionBarActivity {
    private static final String TAG = "EncryptImageActivity";
    final int READ_REQUEST_CODE;
    Uri file;

    public EncryptImageActivity() {
        this.READ_REQUEST_CODE = 42;
    }

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView((int) C0131R.layout.activity_encrypt_image);
    }

    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(C0131R.menu.menu_encrypt_image, menu);
        return true;
    }

    public boolean onOptionsItemSelected(MenuItem item) {
        if (item.getItemId() == C0131R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == 42 && resultCode == -1 && data != null) {
            this.file = data.getData();
            Log.d(TAG, "Uri: " + this.file.toString());
            ((TextView) findViewById(C0131R.id.textview_uri)).setText(this.file.toString());
        }
    }

    public void onSelectFileClicked(View view) {
        Intent intent = new Intent("android.intent.action.OPEN_DOCUMENT");
        intent.addCategory("android.intent.category.OPENABLE");
        intent.setType("image/*");
        startActivityForResult(intent, 42);
    }

    public void onEncryptClicked(View view) {
        String password = ((EditText) findViewById(C0131R.id.text_password)).getText().toString();
        if (password.equals(BuildConfig.FLAVOR)) {
            Toast.makeText(getApplicationContext(), "You must enter a password!", 0).show();
            return;
        }
        byte[] key = md5(password);
        if (this.file.toString().length() == 0) {
            Toast.makeText(getApplicationContext(), "You must select a file!", 0).show();
            return;
        }
        try {
            byte[] cipherText = encryptData(readUri(this.file), key);
            try {
                File outputFile = new File(getOutputPath(), generateRandomFilename(8) + ".encrypted");
                try {
                    FileOutputStream fileOutputStream = new FileOutputStream(outputFile);
                    fileOutputStream.write(cipherText);
                    fileOutputStream.close();
                    Toast.makeText(getApplicationContext(), "Successfully created file " + outputFile.getAbsolutePath(), 1).show();
                } catch (FileNotFoundException e) {
                    Log.e(TAG, "Could not find output directory");
                } catch (IOException e2) {
                    Log.e(TAG, "Unable to write to file");
                }
            } catch (IOException e3) {
                Log.e(TAG, "Unable to connect to external storage");
            }
        } catch (IOException e4) {
            Toast.makeText(getApplicationContext(), "Could not read file", 0).show();
        }
    }

    private File getOutputPath() throws IOException {
        if ("mounted".equals(Environment.getExternalStorageState())) {
            File file = new File(Environment.getExternalStorageDirectory().getAbsolutePath() + "/encryptimage/");
            file.mkdir();
            return file;
        }
        throw new IOException("Error connecting to external media");
    }

    private String generateRandomFilename(int length) {
        Random random = new Random();
        StringBuilder stringBuilder = new StringBuilder(length);
        for (int i = 0; i < length; i++) {
            char temp = (char) random.nextInt(62);
            if (temp < '\u001a') {
                temp = (char) (temp + 97);
            } else if (temp < '4') {
                temp = (char) (temp + 65);
            } else {
                temp = (char) (temp + 48);
            }
            stringBuilder.append(temp);
        }
        return stringBuilder.toString();
    }

    private byte[] readUri(Uri uri) throws IOException {
        InputStream inputStream = getContentResolver().openInputStream(uri);
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        byte[] buffer = new byte[AccessibilityNodeInfoCompat.ACTION_NEXT_HTML_ELEMENT];
        while (true) {
            int read = inputStream.read(buffer);
            if (read == -1) {
                return byteArrayOutputStream.toByteArray();
            }
            byteArrayOutputStream.write(buffer, 0, read);
        }
    }

    private byte[] md5(String data) {
        try {
            MessageDigest messageDigest = MessageDigest.getInstance("md5");
            messageDigest.update(data.getBytes());
            return messageDigest.digest();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return new byte[0];
        }
    }

    private byte[] encryptData(byte[] data, byte[] key) {
        byte keyLength = (byte) key.length;
        byte[] cipherText = new byte[data.length];
        for (int i = 0; i < data.length; i++) {
            cipherText[i] = (byte) (data[i] ^ key[i % keyLength]);
        }
        return cipherText;
    }
}
