#!/usr/bin/env python3
import base64
import hashlib
import time
from datetime import datetime

# ===== YOUR SETTINGS =====
SERVER_IP = "202.166.192.207"
STREAM_NAME = "wc-Himalaya3"
SECRET_KEY = "mypassword123"
# =========================

def generate_link():
    current_time = int(time.time())
    valid_minutes = 1440
    
    auth_string = f"server_time={current_time}&valid_minutes={valid_minutes}&id=200"
    hash_value = hashlib.md5(f"{auth_string}{SECRET_KEY}".encode()).hexdigest()
    
    wms_auth = base64.b64encode(
        f"{auth_string}&hash_value={hash_value}".encode()
    ).decode()
    
    link = f"http://{SERVER_IP}/ffplay/{STREAM_NAME}/playlist.m3u8?wmsAuthSign={wms_auth}"
    
    return link

if __name__ == "__main__":
    link = generate_link()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    readme_content = f"""# 📺 My Streaming Link

## 🌐 Current Link


## ⏰ Generated Time
{current_time}

## ✅ Status
- **Active**: Yes
- **Expiry**: 24 hours

## 🔄 Auto-Refresh
This link automatically refreshes every 24 hours.

## 📥 How to Use
- **VLC**: File → Open Network → Paste link
- **Browser**: Use HLS player
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ Link generated successfully!")
    print(f"📍 {link}")

if __name__ == "__main__":
    generate_link()
