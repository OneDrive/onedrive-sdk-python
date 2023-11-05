# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
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

    async def delete_async(self):
        """Deletes the specified Permission."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        await future

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

    async def get_async(self):
        """Gets the specified Permission in async.

        Yields:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The Permission.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = await future
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

    async def update_async(self, permission):
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
        entity = await future
        return entity

