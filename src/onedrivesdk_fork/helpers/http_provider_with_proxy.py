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
from onedrivesdk import http_provider_base, http_response


class HttpProviderWithProxy(http_provider_base.HttpProviderBase):
    """Use this HttpProvider when you want to proxy your requests.
    For example, if you have an HTTP request capture suite, you
    can use this provider to proxy the requests through that
    capture suite.    
    """

    DEFAULT_PROXIES = {
        'http': 'http://127.0.0.1:8888',
        'https': 'https://127.0.0.1:8888'
    }
    
    def __init__(self, proxies=None, verify_ssl=True):
        """Initializes the provider. Proxy and SSL settings are stored
        in the object and applied to every request.
        
        Args:
            proxies (dict of str:str):
                Mapping of protocols to proxy URLs. See `requests`
                documentation:
                http://docs.python-requests.org/en/latest/api/#requests.request
                If None, HttpProviderWithProxy.DEFAULT_PROXIES is used.
            verify_ssl (bool):
                Whether SSL certs should be verified during
                request proxy.
        """
        self.proxies = proxies if proxies is not None \
            else HttpProviderWithProxy.DEFAULT_PROXIES
        self.verify_ssl = verify_ssl

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
        session = requests.Session()

        if path:
            with open(path, mode='rb') as f:
                request = requests.Request(method,
                                           url,
                                           headers=headers,
                                           data=f)
                prepped = request.prepare()
                response = session.send(prepped,
                                        verify=self.verify_ssl,
                                        proxies=self.proxies)
        else:
            request = requests.Request(method,
                                       url,
                                       headers=headers,
                                       data=data,
                                       json=content)
            prepped = request.prepare()
            response = session.send(prepped,
                                    verify=self.verify_ssl,
                                    proxies=self.proxies)

        custom_response = http_response.HttpResponse(response.status_code, response.headers, response.text)
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
        response = requests.get(
            url,
            stream=True,
            headers=headers,
            verify=self.verify_ssl,
            proxies=self.proxies)

        if response.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            custom_response = http_response.HttpResponse(response.status_code, response.headers, None)
        else:
            custom_response = http_response.HttpResponse(response.status_code, response.headers, response.text)

        return custom_response
