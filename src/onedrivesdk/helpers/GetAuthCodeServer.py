'''
------------------------------------------------------------------------------
 Copyright (c) 2015 Microsoft Corporation

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
------------------------------------------------------------------------------
'''
try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as BaseHTTPRequestHandler
    from SocketServer import TCPServer as HTTPServer

try:
    from urllib.parse import urlparse, parse_qs, unquote
except ImportError:
    from urlparse import urlparse, parse_qs
    from urllib import unquote

import threading
import webbrowser

def get_auth_code(auth_url, redirect_uri):
    """Easy way to get the auth code. Wraps up all the threading
    and stuff. Does block main thread.

    Args:
        auth_url (str): URL of auth server
        redirect_uri (str): Redirect URI, as set for the app. Should be 
            something like "http://localhost:8080" for this to work.

    Returns: 
        str: A string representing the auth code, sent back by the server
    """
    HOST, PORT = urlparse(redirect_uri).netloc.split(':')
    PORT = int(PORT)
    # Set up HTTP server and thread
    code_acquired = threading.Event()
    s = GetAuthCodeServer((HOST, PORT), code_acquired, GetAuthCodeRequestHandler)    
    th = threading.Thread(target=s.serve_forever)
    th.start()
    webbrowser.open(auth_url)
    # At this point the browser will open and the code
    # will be extracted by the server
    code_acquired.wait()  # First wait for the response from the auth server
    code = s.auth_code
    s.shutdown()
    th.join()
    return code


class GetAuthCodeServer(HTTPServer, object):

    def __init__(self, server_address, stop_event, RequestHandlerClass):
        HTTPServer.__init__(self, server_address, RequestHandlerClass)
        self._stop_event = stop_event
        self.auth_code = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
        if value is not None:
            self._stop_event.set()


class GetAuthCodeRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        if "code" in params:
            # Extract the code query param
            self.server.auth_code = params["code"][0]
        if "error" in params:
            error_msg, error_desc = (unquote(params["error"][0]),
                                     unquote(params["error_description"][0]))
            raise RuntimeError("The server returned an error: {} - {}"
                               .format(error_msg, error_desc))
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(
            '<script type="text/javascript">window.close()</script>'
            .encode("utf-8")))
