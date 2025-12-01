#!/usr/bin/env python3
"""
Simple HTTP Server - Sacred Smoke Example
Starts a basic HTTP server that can be accessed from a browser.
"""

import http.server
import socketserver
import sys
from datetime import datetime

PORT = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with enhanced responses."""
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Sacred Smoke - Python on Android</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 50px auto;
                        padding: 20px;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: #333;
                    }}
                    .container {{
                        background: white;
                        padding: 30px;
                        border-radius: 10px;
                        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                    }}
                    h1 {{ color: #667eea; }}
                    .info {{ 
                        background: #f0f0f0; 
                        padding: 10px; 
                        margin: 10px 0;
                        border-radius: 5px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🔥 Sacred Smoke</h1>
                    <h2>Python HTTP Server Running on Android!</h2>
                    <div class="info">
                        <p><strong>Python Version:</strong> {sys.version.split()[0]}</p>
                        <p><strong>Server Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                        <p><strong>Port:</strong> {PORT}</p>
                    </div>
                    <p>This simple HTTP server is running on your Android device using Sacred Smoke.</p>
                    <p>Visit <code>/api</code> for a JSON response.</p>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
            
        elif self.path == '/api':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            import json
            response = {
                'status': 'ok',
                'message': 'Sacred Smoke API',
                'python_version': sys.version,
                'timestamp': datetime.now().isoformat(),
                'port': PORT
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
        else:
            super().do_GET()

def main():
    print("=" * 60)
    print("Sacred Smoke - Simple HTTP Server")
    print("=" * 60)
    print(f"\nStarting server on port {PORT}...")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"\nAccess the server at:")
    print(f"  http://localhost:{PORT}")
    print(f"  http://127.0.0.1:{PORT}")
    print(f"\nAPI endpoint:")
    print(f"  http://localhost:{PORT}/api")
    print("\nPress Ctrl+C to stop the server.")
    print("=" * 60 + "\n")
    
    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        print(f"\n❌ Error: {e}")
        print(f"Port {PORT} may already be in use. Try a different port.")
        sys.exit(1)

if __name__ == "__main__":
    main()
