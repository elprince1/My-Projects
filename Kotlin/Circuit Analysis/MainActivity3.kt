package com.elprince.startup

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
var k=0
class MainActivity3 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        if (k == 0) {
            setContentView(R.layout.activity_main3)
            Handler().postDelayed({
                finish()
                val intent2 = Intent(this, MainActivity::class.java)
                startActivity(intent2)

            }, 3000)
            k = 1
        }
    }
}