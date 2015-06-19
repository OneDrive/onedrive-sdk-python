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
import abc


class AuthProviderBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, http_provider, client_id, scopes, access_token):
        pass

    @property
    def client_id(self):
        pass

    @client_id.setter
    @abc.abstractmethod
    def client_id(self, value):
        pass

    @property
    def scopes(self):
        pass

    @scopes.setter
    @abc.abstractmethod
    def scopes(self, value):
        pass

    @property
    def access_token(self):
        pass

    @access_token.setter
    @abc.abstractmethod
    def access_token(self, value):
        pass

    @abc.abstractmethod
    def get_auth_url(self, auth_server_url, redirect_uri):
        pass

    @abc.abstractmethod
    def authenticate(self, code, auth_server_url, redirect_uri, client_secret):
        pass

    @abc.abstractmethod
    def authenticate_request(self, request):
        pass

    @abc.abstractmethod
    def refresh_token(self):
        pass
