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

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
import json
import asyncio

class EffectiveRolesCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the EffectiveRolesCollectionRequest
        
        Args:
            request_url (str): The url to perform the EffectiveRolesCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(EffectiveRolesCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the EffectiveRolesCollectionPage

        Returns: 
            :class:`EffectiveRolesCollectionPage<onedrivesdk.request.effective_roles_collection.EffectiveRolesCollectionPage>`:
                The EffectiveRolesCollectionPage
        """
        self.method = "GET"
        collection_response = EffectiveRolesCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    async def get_async(self):
        """Gets the EffectiveRolesCollectionPage in async

        Yields: 
            :class:`EffectiveRolesCollectionPage<onedrivesdk.request.effective_roles_collection.EffectiveRolesCollectionPage>`:
                The EffectiveRolesCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class EffectiveRolesCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the strRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a strRequestBuilder for
        
        Returns: 
            :class:`strRequestBuilder<onedrivesdk.request.str_request_builder.strRequestBuilder>`:
                A strRequestBuilder for that key
        """
        return strRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the EffectiveRolesCollectionRequest
        
        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-seperated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`EffectiveRolesCollectionRequest<onedrivesdk.request.effective_roles_collection.EffectiveRolesCollectionRequest>`:
                The EffectiveRolesCollectionRequest
        """
        req = EffectiveRolesCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the EffectiveRolesCollectionPage

        Returns: 
            :class:`EffectiveRolesCollectionPage<onedrivesdk.request.effective_roles_collection.EffectiveRolesCollectionPage>`:
                The EffectiveRolesCollectionPage
        """
        return self.request().get()

    async def get_async(self):
        """Gets the EffectiveRolesCollectionPage in async

        Yields: 
            :class:`EffectiveRolesCollectionPage<onedrivesdk.request.effective_roles_collection.EffectiveRolesCollectionPage>`:
                The EffectiveRolesCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class EffectiveRolesCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`EffectiveRolesCollectionPage<onedrivesdk.request.effective_roles_collection.EffectiveRolesCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = EffectiveRolesCollectionPage(self._prop_dict["value"])

        return self._collection_page


class EffectiveRolesCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the str at the index specified
        
        Args:
            index (int): The index of the item to get from the EffectiveRolesCollectionPage

        Returns:
            :class:`str<onedrivesdk.model.str.str>`:
                The str at the index
        """
        return str(self._prop_list[index])

    def effective_roles(self):
        """Get a generator of str within the EffectiveRolesCollectionPage
        
        Yields:
            :class:`str<onedrivesdk.model.str.str>`:
                The next str in the collection
        """
        for item in self._prop_list:
            yield str(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the EffectiveRolesCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`OneDriveClient<onedrivesdk.model.one_drive_client.OneDriveClient>`:
                The client to be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`:
                A list of options
        """
        self._next_page_request = EffectiveRolesCollectionRequest(next_page_link, client, options)


from ..request.str_request_builder import strRequestBuilder
