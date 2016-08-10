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
from __future__ import unicode_literals
import json
from .auth_provider_base import AuthProviderBase
from .options import *
from .session import Session
import sys

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
from requests_ntlm import HttpNtlmAuth
from .ntlm_http_provider import NtlmHttpProvider

class NtlmAuthProvider(AuthProviderBase):

    AUTH_SERVER_URL = "https://login.live.com/oauth20_authorize.srf"
    AUTH_TOKEN_URL = "https://login.live.com/oauth20_token.srf"

    def __init__(self, http_provider, client_id=None, scopes=None, access_token=None, session_type=None, loop=None):
        """Initialize the authentication provider for authenticating
        requests sent to OneDrive

        Args:
            http_provider (:class:`NtlmHttpProvider<onedrivesdk.helpers.NtlmHttpProvider>`):
                The HTTP provider to use for all auth requests, must be of corresponding NtlmHttpProvider type
            client_id (str): Defaults to None, the client id for your
                application
            scopes (list of str): Defaults to None, the scopes 
                that are required for your application
            access_token (str): Defaults to None, the access token
                for your application
            session_type (:class:`SessionBase<onedrivesdk.session_base.SessionBase>`):
                Defaults to :class:`Session<onedrivesdk.session.Session>`,
                the implementation of SessionBase that stores your
                session. WARNING: THE DEFAULT IMPLEMENTATION ONLY
                STORES SESSIONS TO THE RUN DIRECTORY IN PLAIN TEXT.
                THIS IS UNSAFE. IT IS HIGHLY RECOMMENDED THAT YOU
                IMPLEMENT YOUR OWN VERSION.
            loop (BaseEventLoop): Defaults to None, the asyncio
                loop to use for all async requests. If none is provided,
                asyncio.get_event_loop() will be called. If using Python
                3.3 or below this does not need to be specified
        """
        if not isinstance(http_provider, NtlmHttpProvider):
            raise RuntimeError('HttpProvider must be an NtlmHttpProvider')
        self._http_provider = http_provider
        self._client_id = client_id
        self._scopes = scopes
        self._access_token = access_token
        self._session_type = Session if session_type is None else session_type
        self._session = None

        if sys.version_info >= (3, 4, 0):
            import asyncio
            self._loop = loop if loop else asyncio.get_event_loop()

    @property
    def client_id(self):
        """Gets and sets the client_id for the
        AuthProvider

        Returns:
            str: The client id
        """
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def scopes(self):
        """Gets and sets the scopes for the
        AuthProvider

        Returns:
            list of str: The scopes
        """
        return self._scopes

    @scopes.setter
    def scopes(self, value):
        self._scopes = value

    @property
    def access_token(self):
        """Gets and sets the access_token for the
        AuthProvider

        Returns:
            str: The access token
        """
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    def get_auth_url(self, redirect_uri):
        """Build the auth url using the params provided
        and the auth_provider

        Args:
            redirect_uri (str): The URI to redirect the response
                to
        """

        params = {
            "client_id": self.client_id,
            "scope": " ".join(self.scopes),
            "response_type": "code",
            "redirect_uri": redirect_uri
            }
        return "{}?{}".format(self.AUTH_SERVER_URL, urlencode(params))

    def authenticate(self, user, password):
        """Store username and password for use in challenges later
        """
        self._username = user
        self._password = password


    def authenticate_request(self):
        """Special function for creating NTLM auth method on HttpProvider.
        """
        if not (hasattr(self, '_username') and hasattr(self, '_password')):
            raise RuntimeError('Username and password must be acquired before authentication.')

        if not hasattr(self._http_provider, '_ntlm_auth_method'):
            self._http_provider._ntlm_auth_method = lambda session: HttpNtlmAuth(self._username, self._password, session)

    def refresh_token(self):
        """Refresh the token currently used by the session"""
        pass

    def save_session(self, **save_session_kwargs):
        """Required by interface, not needed by ntlm implementation
        """
        pass

    def load_session(self, **load_session_kwargs):
        """Required by interface, not needed by ntlm implementation
        """
        pass
