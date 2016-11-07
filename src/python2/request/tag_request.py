# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..request_base import RequestBase
from ..model.tag import Tag
import json

class TagRequest(RequestBase):
    """The type TagRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new TagRequest.

        Args:
            request_url (str): The url to perform the TagRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(TagRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Tag."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Tag.
        
        Returns:
            :class:`Tag<onedrivesdk.model.tag.Tag>`:
                The Tag.
        """
        self.method = "GET"
        entity = Tag(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, tag):
        """Updates the specified Tag.
        
        Args:
            tag (:class:`Tag<onedrivesdk.model.tag.Tag>`):
                The Tag to update.

        Returns:
            :class:`Tag<onedrivesdk.model.tag.Tag>`:
                The updated Tag.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Tag(json.loads(self.send(tag).content))
        self._initialize_collection_properties(entity)
        return entity

