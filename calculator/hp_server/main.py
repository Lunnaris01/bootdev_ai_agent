import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "calculator/hp_server"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
