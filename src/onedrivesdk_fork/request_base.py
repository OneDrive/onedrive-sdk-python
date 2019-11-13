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
from .version import __version__
from .options import *
from .one_drive_object_base import OneDriveObjectBase

try:
    from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
except ImportError:
    from urlparse import urlparse, parse_qsl, urlunparse
    from urllib import urlencode
from collections import OrderedDict

class RequestBase(object):

    def __init__(self, request_url, client, options):
        """Initialize a request to be sent

        Args:
            request_url (str): The URL to send the request to
            client (:class:`OneDriveClient<onedrivesdk.requests.one_drive_client.OneDriveClient>`):
                The client used to make the requests
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to add to the request
        """
        self._client = client
        self._request_url = request_url
        self._headers = {}
        self._query_options = OrderedDict()
        self.content_type = None

        if (options):
            header_list = [
                pair for pair in options if isinstance(pair, HeaderOption)]
            self._headers = {pair.key: pair.value for pair in header_list}

            query_list = [
                pair for pair in options if isinstance(pair, QueryOption)]
            self._query_options = OrderedDict((pair.key, pair.value) for pair in query_list)

    @property
    def request_url(self):
        """Gets the request URL with query string appended

        Returns:
            str: The request URL
        """
        url_parts = list(urlparse(self._request_url))
        query_dict = OrderedDict(parse_qsl(url_parts[4]))
        self._query_options.update(query_dict)
        url_parts[4] = urlencode(self._query_options)
        return urlunparse(url_parts)

    @property
    def content_type(self):
        """Gets and sets the content-type header of the request
        (ex. application/x-www-form-urlencoded)

        Returns:
            str: The request content-type
        """
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value

    @property
    def method(self):
        """Gets and sets the HTTP method by which to send the
        request (ex. PUT, GET)

        Returns:
            str: The HTTP method
        """
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    def append_option(self, option):
        """Appends an option to the request

        Args:
            option (:class:`Option<onedrivesdk.options.Option>`):
                The option to append to the request
        """
        if isinstance(option, HeaderOption):
            self._headers[option.key] = option.value
        elif isinstance(option, QueryOption):
            self._query_options[option.key] = option.value

    def send(self, content=None, path=None, data=None):
        """Send the request using the client specified
        at request initialization

        Args:
            content (str): Defaults to None, the body of the request
                that will be sent
            path (str): Defaults to None, the local path of the file which
                will be sent
            data (file object): Defaults to none, the file object of the
                file which will be sent

        Returns:
            :class:`HttpResponse<onedrivesdk.http_response.HttpResponse>`:
                The response to the request
        """
        self._client.auth_provider.authenticate_request(self)

        self.append_option(HeaderOption("X-RequestStats",
                                        "SDK-Version=python-v"+__version__))

        if self.content_type:
            self.append_option(HeaderOption("Content-Type", self.content_type))

        if path:
            response = self._client.http_provider.send(
                self.method,
                self._headers,
                self.request_url,
                path=path)
        elif data:
            response = self._client.http_provider.send(
                self.method,
                self._headers,
                self.request_url,
                data=data)
        else:
            content_dict = None

            if content:
                content_dict = content.to_dict() if isinstance(
                    content, OneDriveObjectBase) else content

            response = self._client.http_provider.send(
                self.method,
                self._headers,
                self.request_url,
                content=content_dict)

        return response

    def download_item(self, path):
        """Download a file to a local path

        Args:
            path (str): The local path to download the file

        Returns:
            :class:`HttpResponse<onedrivesdk.http_response.HttpResponse>`:
                The response to the request
        """
        self._client.auth_provider.authenticate_request(self)

        self.append_option(HeaderOption("X-RequestStats",
                                        "SDK-Version=python-v"+__version__))

        if self.content_type:
            self.append_option(HeaderOption("Content-Type", self.content_type))

        response = self._client.http_provider.download(
            self._headers,
            self.request_url,
            path)

        return response

    def _set_query_options(self, expand=None, select=None, top=None, order_by=None):
        """Adds query options from a set of known parameters

        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-seperated list of properties
                that are used to sort the order of items in the response.
        """
        if expand:
            self.append_option(QueryOption("expand", expand))

        if select:
            self.append_option(QueryOption("select", select))

        if top:
            self.append_option(QueryOption("top", top))

        if order_by:
            self.append_option(QueryOption("orderby", order_by))
