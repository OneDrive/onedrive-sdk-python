# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase
from ..request_builder_base import RequestBuilderBase
from ..model.shares_collection_page import SharesCollectionPage
import json
import asyncio

class SharesCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the SharesCollectionRequest
        
        Args:
            request_url (str): The url to perform the SharesCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(SharesCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the SharesCollectionPage

        Returns: 
            :class:`SharesCollectionPage<onedrivesdk.request.shares_collection.SharesCollectionPage>`:
                The SharesCollectionPage
        """
        self.method = "GET"
        collection_response = SharesCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the SharesCollectionPage in async

        Yields: 
            :class:`SharesCollectionPage<onedrivesdk.request.shares_collection.SharesCollectionPage>`:
                The SharesCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

    @staticmethod
    def get_next_page_request(collection_page, client, options):
        """Gets the SharesCollectionRequest for the next page. Returns None if there is no next page

        Yields: 
            :class:`SharesCollectionRequest<onedrivesdk.request.shares_collection.SharesCollectionRequest>`:
                The SharesCollectionRequest
        """
        if collection_page._next_page_link:
            return SharesCollectionRequest(collection_page._next_page_link, client, options)
        else:
            return None

class SharesCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ShareRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ShareRequestBuilder for
        
        Returns: 
            :class:`ShareRequestBuilder<onedrivesdk.request.share_request_builder.ShareRequestBuilder>`:
                A ShareRequestBuilder for that key
        """
        return ShareRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the SharesCollectionRequest
        
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
            :class:`SharesCollectionRequest<onedrivesdk.request.shares_collection.SharesCollectionRequest>`:
                The SharesCollectionRequest
        """
        req = SharesCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the SharesCollectionPage

        Returns: 
            :class:`SharesCollectionPage<onedrivesdk.request.shares_collection.SharesCollectionPage>`:
                The SharesCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the SharesCollectionPage in async

        Yields: 
            :class:`SharesCollectionPage<onedrivesdk.request.shares_collection.SharesCollectionPage>`:
                The SharesCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class SharesCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`SharesCollectionPage<onedrivesdk.request.shares_collection.SharesCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = SharesCollectionPage(self._prop_dict["value"])

        return self._collection_page


from ..request.share_request_builder import ShareRequestBuilder
