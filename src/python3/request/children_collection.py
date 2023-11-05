# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase
from ..request_builder_base import RequestBuilderBase
from ..model.children_collection_page import ChildrenCollectionPage
from ..model.item import Item
import json
import asyncio

class ChildrenCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ChildrenCollectionRequest
        
        Args:
            request_url (str): The url to perform the ChildrenCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(ChildrenCollectionRequest, self).__init__(request_url, client, options)

    def add(self, entity):
        """Add a Item to the collection
        
        Args:
            entity (:class:`Item<onedrivesdk.model.item.Item>`):
                The Item that you would like to add to the collection
        
        Returns: 
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item that you added, with additional data from OneDrive
        """
        self.content_type = "application/json"
        self.method = "POST"
        entity = Item(json.loads(self.send(entity).content))
        return entity

    async def add_async(self, entity):
        """Add a Item to the collection in async
        
        Args:
            entity (:class:`Item<onedrivesdk.model.item.Item>`):
                The Item that you would like to add to the collection
        
        Yields: 
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item that you added, with additional data from OneDrive
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.add,
                                                    entity)
        entity = await future
        return entity

    def get(self):
        """Gets the ChildrenCollectionPage

        Returns: 
            :class:`ChildrenCollectionPage<onedrivesdk.model.children_collection_page.ChildrenCollectionPage>`:
                The ChildrenCollectionPage
        """
        self.method = "GET"
        collection_response = ChildrenCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    async def get_async(self):
        """Gets the ChildrenCollectionPage in async

        Yields: 
            :class:`ChildrenCollectionPage<onedrivesdk.model.children_collection_page.ChildrenCollectionPage>`:
                The ChildrenCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = await future
        return collection_page

    @staticmethod
    def get_next_page_request(collection_page, client, options=None):
        """Gets the ChildrenCollectionRequest for the next page. Returns None if there is no next page

        Args:
            collection_page (:class:`ChildrenCollectionPage<onedrivesdk.model.children_collection_page.ChildrenCollectionPage>`):
                The collection to get the next page for
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Yields: 
            :class:`ChildrenCollectionRequest<onedrivesdk.request.children_collection.ChildrenCollectionRequest>`:
                The ChildrenCollectionRequest
        """
        if collection_page._next_page_link:
            return ChildrenCollectionRequest(collection_page._next_page_link, client, options)
        else:
            return None

class ChildrenCollectionRequestBuilder(RequestBuilderBase):

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
        """Builds the ChildrenCollectionRequest
        
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
            :class:`ChildrenCollectionRequest<onedrivesdk.request.children_collection.ChildrenCollectionRequest>`:
                The ChildrenCollectionRequest
        """
        req = ChildrenCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def add(self, entity):
        """Add a Item to the collection
        
        Args:
            entity (:class:`Item<onedrivesdk.model.item.Item>`):
                The Item that you would like to add to the collection
        
        Returns: 
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item that you added, with additional data from OneDrive
        """
        return self.request().add(entity)

    async def add_async(self, entity):
        """Add a Item to the collection in async
        
        Args:
            entity (:class:`Item<onedrivesdk.model.item.Item>`):
                The Item that you would like to add to the collection
        
        Yields: 
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item that you added, with additional data from OneDrive
        """
        entity = await self.request().add_async(entity)
        return entity

    def get(self):
        """Gets the ChildrenCollectionPage

        Returns: 
            :class:`ChildrenCollectionPage<onedrivesdk.model.children_collection_page.ChildrenCollectionPage>`:
                The ChildrenCollectionPage
        """
        return self.request().get()

    async def get_async(self):
        """Gets the ChildrenCollectionPage in async

        Yields: 
            :class:`ChildrenCollectionPage<onedrivesdk.model.children_collection_page.ChildrenCollectionPage>`:
                The ChildrenCollectionPage
        """
        collection_page = await self.request().get_async()
        return collection_page


class ChildrenCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ChildrenCollectionPage<onedrivesdk.model.children_collection_page.ChildrenCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ChildrenCollectionPage(self._prop_dict["value"])

        return self._collection_page


from ..request.item_request_builder import ItemRequestBuilder
