#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get length of posted data
        content_length = int(self.headers.get('Content-Length', 0))

        # Read data and decode it
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Parse parameters into a dict
        params = dict(urllib.parse.parse_qsl(post_data))
        email = params.get("email", "")

        # Build the response
        response = f"Email: {email}"

        # Send headers
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        # Send response body
        self.wfile.write(response.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('0.0.0.0', 5000)
    httpd = HTTPServer(server_address, PostHandler)
    print("Server running on port 5000…")
    httpd.serve_forever()

