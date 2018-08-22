from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
from cowpy import cow
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        # set a status code
        # set any headers
        # set any body data on the response
        # end headers

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Hello world</h1></body></html>')
            return

        elif parsed_path.path == '/tux':
            say = parsed_qs['message'][0]
            cheese = cow.Moose()
            msg = cheese.milk(say)


            self.send_response(200)
            # self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(msg.encode())
            return



        self.send_response(404)
        self.end_headers()


    def do_POST(self):

        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/tux':
            say = parsed_qs['message'][0]
            cheese = cow.Moose()
            msg = cheese.milk(say)
            msg_json = json.dumps({'content': msg})

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(msg_json.encode())
            return


def create_server():
    return HTTPServer(
        ('127.0.0.1', int(os.environ['PORT'])),
        SimpleHTTPRequestHandler
    )


def run_forever():
    server = create_server()

    try:
        print(f'Server running on {os.environ["PORT"]}')
        server.serve_forever()

    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
