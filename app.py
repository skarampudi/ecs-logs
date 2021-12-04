#!/usr/bin/env python

"""A simple HTTP server with REST and json for python 3.

To start: python3 app.py
url: http://0.0.0.0:8000
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import datetime
from json import JSONEncoder
import logging

logging.basicConfig(handlers=[logging.FileHandler(filename="./logs/app.log",
                                                encoding='utf-8',
                                                mode='a+')],
                                                format="%(asctime)s %(name)s:%(levelname)s:%(message)s", 
                                                datefmt="%F %A %T", 
                                                level=logging.INFO)

message = {
    "date": datetime.datetime.now(),
    "message": "Hello, World From Python!"
}

class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        data = json.dumps(message, indent=4, cls=DateTimeEncoder)
        self.wfile.write(data.encode('utf8'))
        logging.info('is when this event was logged.')
        logging.info('is when this request recieved.')

def main():

    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    logging.info('HTTP Server Running...........')
    server.serve_forever()

if __name__ == '__main__':
    main()
