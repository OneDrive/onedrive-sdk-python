# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..request_base import RequestBase
from ..model.thumbnail import Thumbnail
import json

class ThumbnailRequest(RequestBase):
    """The type ThumbnailRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ThumbnailRequest.

        Args:
            request_url (str): The url to perform the ThumbnailRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(ThumbnailRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Thumbnail."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Thumbnail.
        
        Returns:
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The Thumbnail.
        """
        self.method = "GET"
        entity = Thumbnail(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, thumbnail):
        """Updates the specified Thumbnail.
        
        Args:
            thumbnail (:class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`):
                The Thumbnail to update.

        Returns:
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The updated Thumbnail.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Thumbnail(json.loads(self.send(thumbnail).content))
        self._initialize_collection_properties(entity)
        return entity

