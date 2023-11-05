# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase
from ..request_builder_base import RequestBuilderBase
from ..model.drives_collection_page import DrivesCollectionPage
import json
import asyncio

class DrivesCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the DrivesCollectionRequest
        
        Args:
            request_url (str): The url to perform the DrivesCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(DrivesCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the DrivesCollectionPage

        Returns: 
            :class:`DrivesCollectionPage<onedrivesdk.model.drives_collection_page.DrivesCollectionPage>`:
                The DrivesCollectionPage
        """
        self.method = "GET"
        collection_response = DrivesCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    async def get_async(self):
        """Gets the DrivesCollectionPage in async

        Yields: 
            :class:`DrivesCollectionPage<onedrivesdk.model.drives_collection_page.DrivesCollectionPage>`:
                The DrivesCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = await future
        return collection_page

    @staticmethod
    def get_next_page_request(collection_page, client, options=None):
        """Gets the DrivesCollectionRequest for the next page. Returns None if there is no next page

        Args:
            collection_page (:class:`DrivesCollectionPage<onedrivesdk.model.drives_collection_page.DrivesCollectionPage>`):
                The collection to get the next page for
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Yields: 
            :class:`DrivesCollectionRequest<onedrivesdk.request.drives_collection.DrivesCollectionRequest>`:
                The DrivesCollectionRequest
        """
        if collection_page._next_page_link:
            return DrivesCollectionRequest(collection_page._next_page_link, client, options)
        else:
            return None

class DrivesCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the DriveRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a DriveRequestBuilder for
        
        Returns: 
            :class:`DriveRequestBuilder<onedrivesdk.request.drive_request_builder.DriveRequestBuilder>`:
                A DriveRequestBuilder for that key
        """
        return DriveRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the DrivesCollectionRequest
        
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
            :class:`DrivesCollectionRequest<onedrivesdk.request.drives_collection.DrivesCollectionRequest>`:
                The DrivesCollectionRequest
        """
        req = DrivesCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the DrivesCollectionPage

        Returns: 
            :class:`DrivesCollectionPage<onedrivesdk.model.drives_collection_page.DrivesCollectionPage>`:
                The DrivesCollectionPage
        """
        return self.request().get()

    async def get_async(self):
        """Gets the DrivesCollectionPage in async

        Yields: 
            :class:`DrivesCollectionPage<onedrivesdk.model.drives_collection_page.DrivesCollectionPage>`:
                The DrivesCollectionPage
        """
        collection_page = await self.request().get_async()
        return collection_page


class DrivesCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`DrivesCollectionPage<onedrivesdk.model.drives_collection_page.DrivesCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = DrivesCollectionPage(self._prop_dict["value"])

        return self._collection_page


from ..request.drive_request_builder import DriveRequestBuilder
