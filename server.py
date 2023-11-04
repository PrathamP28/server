from http.server import HTTPServer, BaseHTTPRequestHandler
HOST = "192.168.1.5"
PORT = 9999
while True:
    class Pratham(BaseHTTPRequestHandler):

        def do_GET(self):

            file = open('text.txt', 'r')
            a = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(a, "utf-8"))

        def do_POST(self):

            file = open('key.txt', 'r')
            a = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(f"<html><body><h1>hello number {a}</h1></body></html> ", "utf-8"))
            exit()

    server = HTTPServer((HOST, PORT), Pratham)
    print("Server Now Runing... ")

    server.serve_forever()
    server.server_close()

    print("Server Stopped!")
