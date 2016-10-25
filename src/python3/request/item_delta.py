# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..collection_base import CollectionRequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
import asyncio


class ItemDeltaRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options, token=None):
        super(ItemDeltaRequest, self).__init__(request_url, client, options)
        self.method = "GET"

        if token:
            self._query_options["token"] = token

    def get(self):
        """Sends the GET request
        
        Returns:
            :class:`ItemDeltaCollectionResponse<onedrivesdk.request.item_delta_collection.ItemDeltaCollectionResponse>`:
                The resulting collection page from the operation
        """
        collection_response = ItemDeltaCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Sends the GET request using an asyncio coroutine
        
        Yields:
            :class:`ItemDeltaCollectionResponse<onedrivesdk.request.item_delta_collection.ItemDeltaCollectionResponse>`:
                The resulting collection page from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_response = yield from future
        return collection_response
    
    @staticmethod
    def get_next_page_request(collection_page, client, options, token=None):
        """Gets the ItemDeltaRequest for the next page. Returns None if there is no next page

        Yields: 
            :class:`ItemDeltaRequest<onedrivesdk.request.item_delta.ItemDeltaRequest>`:
                The ItemDeltaRequest
        """
        if collection_page._next_page_link:
            return ItemDeltaRequest(collection_page._next_page_link, client, options, token)
        else:
            return None


class ItemDeltaRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, token=None):
        super(ItemDeltaRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["token"] = token

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the request for the ItemDelta
        
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
            :class:`ItemDeltaRequest<onedrivesdk.request.item_delta.ItemDeltaRequest>`:
                The request
        """
        req = ItemDeltaRequest(self._request_url, self._client, options, token=self._method_options["token"])
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Sends the GET request
        
        Returns:
            :class:`ItemDeltaCollectionResponse<onedrivesdk.request.item_delta_collection.ItemDeltaCollectionResponse>`:
            The resulting ItemDeltaCollectionResponse from the operation
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Sends the GET request using an asyncio coroutine
        
        Yields:
            :class:`ItemDeltaCollectionResponse<onedrivesdk.request.item_delta_collection.ItemDeltaCollectionResponse>`:
                The resulting ItemDeltaCollectionResponse from the operation
        """
        collection_page = yield from self.request().get_async()
        return collection_page

from ..request.item_delta_collection import ItemDeltaCollectionResponse
