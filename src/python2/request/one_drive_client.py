# -*- coding: utf-8 -*- 
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
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
------------------------------------------------------------------------------

 This file was generated and any changes will be overwritten.
'''
from __future__ import unicode_literals
from ..request.drives_collection import DrivesCollectionRequestBuilder
from ..request.shares_collection import SharesCollectionRequestBuilder
import sys


class OneDriveClient(object):

    def __init__(self, base_url, auth_provider, http_provider, loop=None):
        """Initialize the :class:`OneDriveClient` to be
            used for all OneDrive API interactions
        
        Args:
            base_url (str): The OneDrive base url to use for API interactions
            auth_provider(:class:`AuthProviderBase<onedrivesdk.auth_provider_base.AuthProviderBase>`):
                The authentication provider used by the client to auth
                with OneDrive services
            http_provider(:class:`HttpProviderBase<onedrivesdk.http_provider_base.HttpProviderBase>`):
                The HTTP provider used by the client to send all 
                requests to OneDrive
            loop (BaseEventLoop): Default to None, the AsyncIO loop 
                to use for all async requests
        """
        self.base_url = base_url
        self.auth_provider = auth_provider
        self.http_provider = http_provider

        if sys.version_info >= (3, 4, 0):
            import asyncio
            self._loop = loop if loop else asyncio.get_event_loop()

    @property
    def auth_provider(self):
        """Gets and sets the client auth provider
        
        Returns:
            :class:`AuthProviderBase<onedrivesdk.auth_provider_base.AuthProviderBase>`: 
            The authentication provider
        """
        return self._auth_provider

    @auth_provider.setter
    def auth_provider(self, value):
        self._auth_provider = value

    @property
    def http_provider(self):
        """Gets and sets the client HTTP provider

        Returns: 
            :class:`HttpProviderBase<onedrivesdk.http_provider_base.HttpProviderBase>`: 
                The HTTP provider
        """
        return self._http_provider

    @http_provider.setter
    def http_provider(self, value):
        self._http_provider = value

    @property
    def base_url(self):
        """Gets and sets the base URL used by the client to make requests

        Returns:
            str: The base URL
        """
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def drives(self):
        """Get the DrivesCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`DrivesCollectionRequestBuilder<onedrivesdk.requests.drives_collection.DrivesCollectionRequestBuilder>`:
                The DrivesCollectionRequestBuilder to return
        """
        return DrivesCollectionRequestBuilder(self.base_url + "drives", self)

    @property
    def shares(self):
        """Get the SharesCollectionRequestBuilder for constructing requests
        
        Returns:
            :class:`SharesCollectionRequestBuilder<onedrivesdk.requests.shares_collection.SharesCollectionRequestBuilder>`:
                The SharesCollectionRequestBuilder to return
        """
        return SharesCollectionRequestBuilder(self.base_url + "shares", self)
