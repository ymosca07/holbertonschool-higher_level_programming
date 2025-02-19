#!/usr/bin/python3
"""Ceci est une description"""
import http.server
import socketserver
import json


class http_SubClass(http.server.BaseHTTPRequestHandler):
    """Ceci est une description"""
    def do_GET(self):
        """Ceci est une description"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode("utf-8"))

        elif self.path == "/info":
            dataset = {"version": "1.0", "description":
                       "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000
with socketserver.TCPServer(("", PORT), http_SubClass) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
