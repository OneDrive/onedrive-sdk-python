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
from ..model.item import Item
import json
import asyncio

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

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Item."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        yield from future

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

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Item in async.

        Yields:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = yield from future
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

    @asyncio.coroutine
    def update_async(self, item):
        """Updates the specified Item in async
        
        Args:
            item (:class:`Item<onedrivesdk.model.item.Item>`):
                The Item to update.

        Yields:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The updated Item.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    item)
        entity = yield from future
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.permissions and value.permissions._prop_dict:
                if "permissions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["permissions@odata.nextLink"]
                    value.permissions._init_next_page_request(next_page_link, self._client, None)
            if value.versions and value.versions._prop_dict:
                if "versions@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["versions@odata.nextLink"]
                    value.versions._init_next_page_request(next_page_link, self._client, None)
            if value.children and value.children._prop_dict:
                if "children@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["children@odata.nextLink"]
                    value.children._init_next_page_request(next_page_link, self._client, None)
            if value.thumbnails and value.thumbnails._prop_dict:
                if "thumbnails@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["thumbnails@odata.nextLink"]
                    value.thumbnails._init_next_page_request(next_page_link, self._client, None)
