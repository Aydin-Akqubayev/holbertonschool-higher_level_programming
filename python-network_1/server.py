#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests"""
        response = "This server is running and ready to receive GET requests!"
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

    def do_POST(self):
        """Handle POST requests for /post_email endpoint"""
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")

        # Parse parameters
        params = dict(urllib.parse.parse_qsl(post_data))
        email = params.get("email", "")

        response = f"Email: {email}"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

if __name__ == "__main__":
    server_address = ("0.0.0.0", 5000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on http://0.0.0.0:5000 …")
    httpd.serve_forever()
