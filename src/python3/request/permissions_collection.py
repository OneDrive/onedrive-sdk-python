# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase
from ..request_builder_base import RequestBuilderBase
from ..model.permissions_collection_page import PermissionsCollectionPage
import json
import asyncio

class PermissionsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the PermissionsCollectionRequest
        
        Args:
            request_url (str): The url to perform the PermissionsCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(PermissionsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the PermissionsCollectionPage

        Returns: 
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The PermissionsCollectionPage
        """
        self.method = "GET"
        collection_response = PermissionsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the PermissionsCollectionPage in async

        Yields: 
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The PermissionsCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

    @staticmethod
    def get_next_page_request(collection_page, client, options=None):
        """Gets the PermissionsCollectionRequest for the next page. Returns None if there is no next page

        Yields: 
            :class:`PermissionsCollectionRequest<onedrivesdk.request.permissions_collection.PermissionsCollectionRequest>`:
                The PermissionsCollectionRequest
        """
        if collection_page._next_page_link:
            return PermissionsCollectionRequest(collection_page._next_page_link, client, options)
        else:
            return None

class PermissionsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the PermissionRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a PermissionRequestBuilder for
        
        Returns: 
            :class:`PermissionRequestBuilder<onedrivesdk.request.permission_request_builder.PermissionRequestBuilder>`:
                A PermissionRequestBuilder for that key
        """
        return PermissionRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the PermissionsCollectionRequest
        
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
            :class:`PermissionsCollectionRequest<onedrivesdk.request.permissions_collection.PermissionsCollectionRequest>`:
                The PermissionsCollectionRequest
        """
        req = PermissionsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the PermissionsCollectionPage

        Returns: 
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The PermissionsCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the PermissionsCollectionPage in async

        Yields: 
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The PermissionsCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class PermissionsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = PermissionsCollectionPage(self._prop_dict["value"])

        return self._collection_page


from ..request.permission_request_builder import PermissionRequestBuilder
