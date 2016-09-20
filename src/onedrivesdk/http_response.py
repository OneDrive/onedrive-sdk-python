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
from __future__ import generators, unicode_literals
import json
from .error import OneDriveError


class HttpResponse(object):

    def __init__(self, status, headers, content):
        """Initialize the HttpResponse class returned after
        an HTTP request is made

        Args:
            status (int): HTTP status (ex. 200, 201, etc.)
            headers (dict of (str, str)): The headers in the
                response
            content (str): The body of the response
        """
        self._status = status
        self._headers = headers
        self._content = content

        if self.content and (self.status < 200 or self.status >= 300):
            try:
                message = json.loads(self.content)
            except ValueError:  # Invalid or empty response message
                message = {}

            if "error" in message:
                if type(message["error"]) == dict:
                    raise OneDriveError(message["error"], self.status)
                else:
                    raise Exception(str(message["error"]))
            else:
                raise OneDriveError("Invalid or empty HttpResponseBody", self.status)

    def __str__(self):
        properties = {
            'Status': self.status,
            'Headers': self.headers,
            'Content': self.content
            }
        ret = ""
        for k, v in properties.items():
            ret += "{}: {}\n".format(k, v)
        return ret

    @property
    def status(self):
        """The HTTP status of the response

        Returns:
            int: HTTP status
        """
        return self._status

    @property
    def headers(self):
        """The headers of the response

        Returns:
            dict of (str, str):
                The headers used by the response
        """
        return self._headers

    @property
    def content(self):
        """The content of the response

        Returns:
            str: The body of the response
        """
        return self._content
