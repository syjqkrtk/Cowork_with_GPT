package com.example.client

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import java.net.Socket

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Thread(Runnable {
            val host = "172.30.1.92"
            val port = 12345
            val socket = Socket(host, port)
            try {
                val inputStream = socket.getInputStream()
                val buffer = ByteArray(1024)
                while (true) {
                    val read = inputStream.read(buffer)
                    val result = String(buffer, 0, read, Charsets.UTF_8)

                    runOnUiThread {
                        val cpuUsageText = findViewById<TextView>(R.id.cpu_usage_text)
                        if (result.isNotEmpty()) {
                            cpuUsageText.text = "CPU usage: $result"
                        }
                    }
                }
            } finally {
                socket.close()
            }
        }).start()
    }
}