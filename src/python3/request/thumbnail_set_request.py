# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..request_base import RequestBase
from ..model.thumbnail_set import ThumbnailSet
import json
import asyncio

class ThumbnailSetRequest(RequestBase):
    """The type ThumbnailSetRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ThumbnailSetRequest.

        Args:
            request_url (str): The url to perform the ThumbnailSetRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(ThumbnailSetRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified ThumbnailSet."""
        self.method = "DELETE"
        self.send()

    async def delete_async(self):
        """Deletes the specified ThumbnailSet."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        await future

    def get(self):
        """Gets the specified ThumbnailSet.
        
        Returns:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The ThumbnailSet.
        """
        self.method = "GET"
        entity = ThumbnailSet(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    async def get_async(self):
        """Gets the specified ThumbnailSet in async.

        Yields:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The ThumbnailSet.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = await future
        return entity

    def update(self, thumbnail_set):
        """Updates the specified ThumbnailSet.
        
        Args:
            thumbnail_set (:class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`):
                The ThumbnailSet to update.

        Returns:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The updated ThumbnailSet.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = ThumbnailSet(json.loads(self.send(thumbnail_set).content))
        self._initialize_collection_properties(entity)
        return entity

    async def update_async(self, thumbnail_set):
        """Updates the specified ThumbnailSet in async
        
        Args:
            thumbnail_set (:class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`):
                The ThumbnailSet to update.

        Yields:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The updated ThumbnailSet.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    thumbnail_set)
        entity = await future
        return entity

