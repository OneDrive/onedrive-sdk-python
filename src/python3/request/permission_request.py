# -*- coding: utf-8 -*- 
'''
# Copyright (c) 2015 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..request_base import RequestBase
from ..model.permission import Permission
import json
import asyncio

class PermissionRequest(RequestBase):
    """The type PermissionRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new PermissionRequest.

        Args:
            request_url (str): The url to perform the PermissionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(PermissionRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Permission."""
        self.method = "DELETE"
        self.send()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Permission."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

    def get(self):
        """Gets the specified Permission.
        
        Returns:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The Permission.
        """
        self.method = "GET"
        entity = Permission(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Permission in async.

        Yields:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The Permission.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
        return entity

    def update(self, permission):
        """Updates the specified Permission.
        
        Args:
            permission (:class:`Permission<onedrivesdk.model.permission.Permission>`):
                The Permission to update.

        Returns:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The updated Permission.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Permission(json.loads(self.send(permission).content))
        self._initialize_collection_properties(entity)
        return entity

    @asyncio.coroutine
    def update_async(self, permission):
        """Updates the specified Permission in async
        
        Args:
            permission (:class:`Permission<onedrivesdk.model.permission.Permission>`):
                The Permission to update.

        Yields:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The updated Permission.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    permission)
        entity = yield from future
        return entity

