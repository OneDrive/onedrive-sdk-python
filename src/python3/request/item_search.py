# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..model.item import Item
from ..collection_base import CollectionRequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
import asyncio


class ItemSearchRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options, q=None):
        super(ItemSearchRequest, self).__init__(request_url, client, options)
        self.method = "GET"

        if q:
            self._query_options["q"] = q

    def get(self):
        """Sends the GET request
        
        Returns:
            :class:`ItemsCollectionResponse<onedrivesdk.request.items_collection.ItemsCollectionResponse>`:
                The resulting collection page from the operation
        """
        collection_response = ItemsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Sends the GET request using an asyncio coroutine
        
        Yields:
            :class:`ItemsCollectionResponse<onedrivesdk.request.items_collection.ItemsCollectionResponse>`:
                The resulting collection page from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_response = yield from future
        return collection_response
    
    @staticmethod
    def get_next_page_request(collection_page, client, options, q=None):
        """Gets the ItemSearchRequest for the next page. Returns None if there is no next page

        Yields: 
            :class:`ItemSearchRequest<onedrivesdk.request.item_search.ItemSearchRequest>`:
                The ItemSearchRequest
        """
        if collection_page._next_page_link:
            return ItemSearchRequest(collection_page._next_page_link, client, options, token)
        else:
            return None


class ItemSearchRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, q=None):
        super(ItemSearchRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["q"] = q

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the request for the ItemSearch
        
        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-seperated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`ItemSearchRequest<onedrivesdk.request.item_search.ItemSearchRequest>`:
                The request
        """
        req = ItemSearchRequest(self._request_url, self._client, options, q=self._method_options["q"])
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Sends the GET request
        
        Returns:
            :class:`ItemsCollectionResponse<onedrivesdk.request.items_collection.ItemsCollectionResponse>`:
            The resulting ItemsCollectionResponse from the operation
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Sends the GET request using an asyncio coroutine
        
        Yields:
            :class:`ItemsCollectionResponse<onedrivesdk.request.items_collection.ItemsCollectionResponse>`:
                The resulting ItemsCollectionResponse from the operation
        """
        collection_page = yield from self.request().get_async()
        return collection_page

from ..request.items_collection import ItemsCollectionResponse
