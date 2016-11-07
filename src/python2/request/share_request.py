# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..request_base import RequestBase
from ..model.share import Share
import json

class ShareRequest(RequestBase):
    """The type ShareRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ShareRequest.

        Args:
            request_url (str): The url to perform the ShareRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(ShareRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Share."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Share.
        
        Returns:
            :class:`Share<onedrivesdk.model.share.Share>`:
                The Share.
        """
        self.method = "GET"
        entity = Share(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, share):
        """Updates the specified Share.
        
        Args:
            share (:class:`Share<onedrivesdk.model.share.Share>`):
                The Share to update.

        Returns:
            :class:`Share<onedrivesdk.model.share.Share>`:
                The updated Share.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Share(json.loads(self.send(share).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.items:
                if "items@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["items@odata.nextLink"]
                    value.items._next_page_link = next_page_link
