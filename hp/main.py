from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        # Ensure that we handle requests for the root path by serving index.html
        # and other paths by serving files directly. 
        # For any other path, we use the default behavior.
        return SimpleHTTPRequestHandler.do_GET(self)

def run():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()