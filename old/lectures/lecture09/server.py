from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # http://localhost:8000/hello/?name=Mumin
        if self.path.startswith("/hello"):
            purl = urlparse(self.path)
            params = parse_qs(purl.query)
            if "name" in params:
              resp = f"Hello, {params['name'][0]}!\n"
            else:
              resp = f"Hello, world!\n"
            self.send_response(200)
            self.end_headers()
            self.wfile.write(resp.encode())

        # http://localhost:8000/bye/
        elif self.path.startswith("/bye"):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Goodbye")

        # Catch-all
        else:
            self.send_error(404)

if __name__ == "__main__":
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f'Listening on {server_address}...')
    httpd.serve_forever() # this will never terminate!
