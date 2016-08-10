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
from __future__ import unicode_literals, with_statement
import requests
from ..http_provider_base import HttpProviderBase
from ..http_response import HttpResponse
from requests_ntlm import HttpNtlmAuth


class NtlmHttpProvider(HttpProviderBase):

    def send(self, method, headers, url, data=None, content=None, path=None):
        """Send the built request using all the specified
        parameters.

        Args:
            method (str): The HTTP method to use (ex. GET)
            headers (dict of (str, str)): A dictionary of name-value
                pairs for headers in the request
            url (str): The URL for the request to be sent to
            data (str): Defaults to None, data to include in the body
                of the request which is not in JSON format
            content (dict): Defaults to None, a dictionary to include
                in JSON format in the body of the request
            path (str): Defaults to None, the path to the local file
                to send in the body of the request

        Returns:
            :class:`HttpResponse<onedrivesdk.http_response.HttpResponse>`:
                The response to the request
        """
        self._setup_session()

        if path:
            with open(path, mode='rb') as f:
                request = requests.Request(method,
                                           url,
                                           headers=headers,
                                           data=f)
                prepped = request.prepare()
                response = self._session.send(prepped)
        else:
            request = requests.Request(method,
                                       url,
                                       headers=headers,
                                       data=data,
                                       json=content)
            prepped = request.prepare()
            response = self._session.send(prepped)

        custom_response = HttpResponse(response.status_code, response.headers, response.text)
        return custom_response

    def download(self, headers, url, path):
        """Downloads a file to the stated path

        Args:
            headers (dict of (str, str)): A dictionary of name-value
                pairs to be used as headers in the request
            url (str): The URL from which to download the file
            path (str): The local path to save the downloaded file

        Returns:
            :class:`HttpResponse<onedrivesdk.http_response.HttpResponse>`:
                The response to the request
        """
        self._setup_session()
        response = self._session.get(
            url,
            stream=True,
            headers=headers)

        if response.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            custom_response = HttpResponse(response.status_code, response.headers, None)
        else:
            custom_response = HttpResponse(response.status_code, response.headers, response.text)

        return custom_response

    def _setup_session(self):
        """
        Internal method for setting up NTLM session
        """
        if not hasattr(self, '_ntlm_auth_method'):
            raise RuntimeError('Session not authenticated. Are you using NtlmAuthProvider?')
        if not hasattr(self, '_session'):
            self._session = requests.Session()
            self._session.auth = self._ntlm_auth_method(self._session)
