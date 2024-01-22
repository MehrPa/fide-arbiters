from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 3000

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write("<html><head><title>Hello, World!</title></head>".encode('utf-8'))
        self.wfile.write("<body><h1>Hello, World!</h1></body></html>".encode('utf-8'))

server = HTTPServer(("", PORT), HelloWorldHandler)
print("Starting server on port {}".format(PORT))
server.serve_forever()
