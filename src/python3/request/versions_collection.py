# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase
from ..request_builder_base import RequestBuilderBase
from ..model.versions_collection_page import VersionsCollectionPage
import json
import asyncio

class VersionsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the VersionsCollectionRequest
        
        Args:
            request_url (str): The url to perform the VersionsCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(VersionsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the VersionsCollectionPage

        Returns: 
            :class:`VersionsCollectionPage<onedrivesdk.model.versions_collection_page.VersionsCollectionPage>`:
                The VersionsCollectionPage
        """
        self.method = "GET"
        collection_response = VersionsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    async def get_async(self):
        """Gets the VersionsCollectionPage in async

        Yields: 
            :class:`VersionsCollectionPage<onedrivesdk.model.versions_collection_page.VersionsCollectionPage>`:
                The VersionsCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = await future
        return collection_page

    @staticmethod
    def get_next_page_request(collection_page, client, options=None):
        """Gets the VersionsCollectionRequest for the next page. Returns None if there is no next page

        Args:
            collection_page (:class:`VersionsCollectionPage<onedrivesdk.model.versions_collection_page.VersionsCollectionPage>`):
                The collection to get the next page for
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Yields: 
            :class:`VersionsCollectionRequest<onedrivesdk.request.versions_collection.VersionsCollectionRequest>`:
                The VersionsCollectionRequest
        """
        if collection_page._next_page_link:
            return VersionsCollectionRequest(collection_page._next_page_link, client, options)
        else:
            return None

class VersionsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ItemRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ItemRequestBuilder for
        
        Returns: 
            :class:`ItemRequestBuilder<onedrivesdk.request.item_request_builder.ItemRequestBuilder>`:
                A ItemRequestBuilder for that key
        """
        return ItemRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the VersionsCollectionRequest
        
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
            :class:`VersionsCollectionRequest<onedrivesdk.request.versions_collection.VersionsCollectionRequest>`:
                The VersionsCollectionRequest
        """
        req = VersionsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the VersionsCollectionPage

        Returns: 
            :class:`VersionsCollectionPage<onedrivesdk.model.versions_collection_page.VersionsCollectionPage>`:
                The VersionsCollectionPage
        """
        return self.request().get()

    async def get_async(self):
        """Gets the VersionsCollectionPage in async

        Yields: 
            :class:`VersionsCollectionPage<onedrivesdk.model.versions_collection_page.VersionsCollectionPage>`:
                The VersionsCollectionPage
        """
        collection_page = await self.request().get_async()
        return collection_page


class VersionsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`VersionsCollectionPage<onedrivesdk.model.versions_collection_page.VersionsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = VersionsCollectionPage(self._prop_dict["value"])

        return self._collection_page


from ..request.item_request_builder import ItemRequestBuilder
