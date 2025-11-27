from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/hello"):
            purl = urlparse(self.path)
            params = parse_qs(purl.query)
            resp = f"Hello, {params.get('name', ['person'])[0]}\n"
            self.send_response(200)
            self.end_headers()
            self.wfile.write(resp.encode())
        elif self.path == "/bye":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Goodbye")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

if __name__ == "__main__":
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f'Listening on {server_address}...')
    httpd.serve_forever()
