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
import asyncio
from ..auth_provider import AuthProvider


async def authenticate_async(self, code, redirect_uri, client_secret=None):
    """Takes in a code string, gets the access token,
    and creates session property bag in async

    Args:
        code (str):
            The code provided by the oauth provider
        redirect_uri (str): The URI to redirect the callback
            to
        client_secret (str): Defaults to None, the client
            secret of your app
    """
    future = self._loop.run_in_executor(None,
                                        self.authenticate,
                                        code,
                                        redirect_uri,
                                        client_secret)
    await future


async def authenticate_request_async(self, request):
    """Authenticate and append the required
    headers to the request in async

    Args:
        request (:class:`RequestBase<onedrivesdk.request_base.RequestBase>`):
            The request to authenticate
    """
    future = self._loop.run_in_executor(None,
                                        self.authenticate_request,
                                        request)
    await future


async def refresh_token_async(self):
    """Refresh the token currently used by the session"""
    future = self._loop.run_in_executor(None,
                                        self.refresh_token)
    await future

AuthProvider.authenticate_async = authenticate_async
AuthProvider.authenticate_request_async = authenticate_async
AuthProvider.refresh_token_async = authenticate_async
