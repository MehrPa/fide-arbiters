from http.server import HTTPServer, SimpleHTTPRequestHandler
import re

PORT = 8000

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            html = """
            <html>
            <head><title>Enter Your Name</title></head>
            <body>
            <form method="POST" action="/res">
                <label for="name">Enter your name: </label>
                <input type="text" id="name" name="name" required>
                <input type="submit" value="Greet Me">
            </form>
            </body>
            </html>
            """.encode('utf-8')

            self.wfile.write(html)
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            try:
                # Extract the name from the POST request body
                name = re.search(r'name=(\w+)', self.headers['Content-Type']).group(1)
            except:
                name = None

            # Greet the user with their name
            greeting = "Hello, {}".format(name) if name else "Hello, Friend!"

            html = """
            <html>
            <head><title>Greetings</title></head>
            <body>
                <h1>{}</h1>
            </body>
            </html>
            """.format(greeting).encode('utf-8')

            self.wfile.write(html)

server = HTTPServer(("", PORT), HelloWorldHandler)
print("Starting server on port {}".format(PORT))
server.serve_forever()
