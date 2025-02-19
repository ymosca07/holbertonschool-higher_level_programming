import json
from http.server import BaseHTTPRequestHandler, HTTPServer
"""Ceci est une description"""


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Ceci est une description"""

    def do_GET(self):
        """Ceci est une description"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    def do_POST(self):
        """Ceci est une description"""
        if self.path == "/message":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {"message": "Received", "data": post_data}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


server_address = ("", 8000)
httpd = HTTPServer(server_address, SimpleAPIHandler)
print("Server running on port 8000...")
httpd.serve_forever()
