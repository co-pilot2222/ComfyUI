from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Security-Policy', "default-src 'self'")
        self.end_headers()
        self.wfile.write(b'<!DOCTYPE html><html><head><title>Blocked Third-Party Resources</title></head><body><h1>Third-Party Resources Blocked</h1><p>This page blocks third-party resources.</p></body></html>')

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

run_server()
