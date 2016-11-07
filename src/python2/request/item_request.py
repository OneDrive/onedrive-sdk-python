# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..request_base import RequestBase
from ..model.item import Item
import json

class ItemRequest(RequestBase):
    """The type ItemRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ItemRequest.

        Args:
            request_url (str): The url to perform the ItemRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(ItemRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Item."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Item.
        
        Returns:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item.
        """
        self.method = "GET"
        entity = Item(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, item):
        """Updates the specified Item.
        
        Args:
            item (:class:`Item<onedrivesdk.model.item.Item>`):
                The Item to update.

        Returns:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The updated Item.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Item(json.loads(self.send(item).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.permissions:
                if "permissions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["permissions@odata.nextLink"]
                    value.permissions._next_page_link = next_page_link
            if value.subscriptions:
                if "subscriptions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["subscriptions@odata.nextLink"]
                    value.subscriptions._next_page_link = next_page_link
            if value.versions:
                if "versions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["versions@odata.nextLink"]
                    value.versions._next_page_link = next_page_link
            if value.children:
                if "children@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["children@odata.nextLink"]
                    value.children._next_page_link = next_page_link
            if value.tags:
                if "tags@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["tags@odata.nextLink"]
                    value.tags._next_page_link = next_page_link
            if value.thumbnails:
                if "thumbnails@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["thumbnails@odata.nextLink"]
                    value.thumbnails._next_page_link = next_page_link
