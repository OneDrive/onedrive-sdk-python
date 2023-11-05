# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase
from ..request_builder_base import RequestBuilderBase
from ..model.subscriptions_collection_page import SubscriptionsCollectionPage
import json
import asyncio

class SubscriptionsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the SubscriptionsCollectionRequest
        
        Args:
            request_url (str): The url to perform the SubscriptionsCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(SubscriptionsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the SubscriptionsCollectionPage

        Returns: 
            :class:`SubscriptionsCollectionPage<onedrivesdk.model.subscriptions_collection_page.SubscriptionsCollectionPage>`:
                The SubscriptionsCollectionPage
        """
        self.method = "GET"
        collection_response = SubscriptionsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    async def get_async(self):
        """Gets the SubscriptionsCollectionPage in async

        Yields: 
            :class:`SubscriptionsCollectionPage<onedrivesdk.model.subscriptions_collection_page.SubscriptionsCollectionPage>`:
                The SubscriptionsCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = await future
        return collection_page

    @staticmethod
    def get_next_page_request(collection_page, client, options=None):
        """Gets the SubscriptionsCollectionRequest for the next page. Returns None if there is no next page

        Args:
            collection_page (:class:`SubscriptionsCollectionPage<onedrivesdk.model.subscriptions_collection_page.SubscriptionsCollectionPage>`):
                The collection to get the next page for
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Yields: 
            :class:`SubscriptionsCollectionRequest<onedrivesdk.request.subscriptions_collection.SubscriptionsCollectionRequest>`:
                The SubscriptionsCollectionRequest
        """
        if collection_page._next_page_link:
            return SubscriptionsCollectionRequest(collection_page._next_page_link, client, options)
        else:
            return None

class SubscriptionsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the SubscriptionRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a SubscriptionRequestBuilder for
        
        Returns: 
            :class:`SubscriptionRequestBuilder<onedrivesdk.request.subscription_request_builder.SubscriptionRequestBuilder>`:
                A SubscriptionRequestBuilder for that key
        """
        return SubscriptionRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the SubscriptionsCollectionRequest
        
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
            :class:`SubscriptionsCollectionRequest<onedrivesdk.request.subscriptions_collection.SubscriptionsCollectionRequest>`:
                The SubscriptionsCollectionRequest
        """
        req = SubscriptionsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the SubscriptionsCollectionPage

        Returns: 
            :class:`SubscriptionsCollectionPage<onedrivesdk.model.subscriptions_collection_page.SubscriptionsCollectionPage>`:
                The SubscriptionsCollectionPage
        """
        return self.request().get()

    async def get_async(self):
        """Gets the SubscriptionsCollectionPage in async

        Yields: 
            :class:`SubscriptionsCollectionPage<onedrivesdk.model.subscriptions_collection_page.SubscriptionsCollectionPage>`:
                The SubscriptionsCollectionPage
        """
        collection_page = await self.request().get_async()
        return collection_page


class SubscriptionsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`SubscriptionsCollectionPage<onedrivesdk.model.subscriptions_collection_page.SubscriptionsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = SubscriptionsCollectionPage(self._prop_dict["value"])

        return self._collection_page


from ..request.subscription_request_builder import SubscriptionRequestBuilder
