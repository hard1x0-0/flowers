#!/usr/bin/env python3
from pyngrok import ngrok
import http.server
import socketserver
import os
import threading
import time

# Change to the correct directory
os.chdir('d:\\codeground\\C++')

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    pass

def start_server():
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server started on http://localhost:{PORT}")
        httpd.serve_forever()

# Start server in background
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Give server time to start
time.sleep(1)

# Create ngrok tunnel
print("Creating public tunnel...")
public_url = ngrok.connect(PORT)
print("\n" + "="*60)
print("✅ YOUR PUBLIC LINK (accessible from anywhere):")
print("="*60)
print(f"\n🌐 {public_url}/flowers2.html\n")
print("="*60)
print("\nShare this link with anyone - they can open it on their phone!")
print("Press Ctrl+C to stop the server\n")

# Keep running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...")
    ngrok.kill()
