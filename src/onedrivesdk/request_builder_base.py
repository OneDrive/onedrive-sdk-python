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


class RequestBuilderBase(object):

    def __init__(self, request_url, client):
        """Initialize a request builder which returns a request
        when request() is called

        Args:
            request_url (str): The URL to construct the request
                for
            client (:class:`OneDriveClient<onedrivesdk.requests.one_drive_client.OneDriveClient>`):
                The client with which the request will be made
        """
        self._request_url = request_url
        self._client = client

    def append_to_request_url(self, url_segment):
        """Appends a URL portion to the current request URL

        Args:
            url_segment (str): The segment you would like to append
                to the existing request URL.
        """
        return self._request_url + "/" + url_segment
