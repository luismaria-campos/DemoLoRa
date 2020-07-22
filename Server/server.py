#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        
        request_path = self.path
        
        print("\n----- Request Start ----->")
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        temperature = self.rfile.read(length)
        print("Temperature: " + temperature)
        print("<----- Request End -----")
        
        self.send_response(200)
    
    do_PUT = do_POST
        
def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()
   
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any POST request\n"
                    "Run: server.py")
    (options, args) = parser.parse_args()
    
    main()