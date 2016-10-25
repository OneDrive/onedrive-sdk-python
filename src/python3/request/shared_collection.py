# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase
from ..request_builder_base import RequestBuilderBase
from ..model.shared_collection_page import SharedCollectionPage
import json

class SharedCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the SharedCollectionRequest
        
        Args:
            request_url (str): The url to perform the SharedCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(SharedCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the SharedCollectionPage

        Returns: 
            :class:`SharedCollectionPage<onedrivesdk.model.shared_collection_page.SharedCollectionPage>`:
                The SharedCollectionPage
        """
        self.method = "GET"
        collection_response = SharedCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


    @staticmethod
    def get_next_page_request(collection_page, client, options=None):
        """Gets the SharedCollectionRequest for the next page. Returns None if there is no next page

        Args:
            collection_page (:class:`SharedCollectionPage<onedrivesdk.model.shared_collection_page.SharedCollectionPage>`):
                The collection to get the next page for
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Yields: 
            :class:`SharedCollectionRequest<onedrivesdk.request.shared_collection.SharedCollectionRequest>`:
                The SharedCollectionRequest
        """
        if collection_page._next_page_link:
            return SharedCollectionRequest(collection_page._next_page_link, client, options)
        else:
            return None

class SharedCollectionRequestBuilder(RequestBuilderBase):

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
        """Builds the SharedCollectionRequest
        
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
            :class:`SharedCollectionRequest<onedrivesdk.request.shared_collection.SharedCollectionRequest>`:
                The SharedCollectionRequest
        """
        req = SharedCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the SharedCollectionPage

        Returns: 
            :class:`SharedCollectionPage<onedrivesdk.model.shared_collection_page.SharedCollectionPage>`:
                The SharedCollectionPage
        """
        return self.request().get()



class SharedCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`SharedCollectionPage<onedrivesdk.model.shared_collection_page.SharedCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = SharedCollectionPage(self._prop_dict["value"])

        return self._collection_page


from ..request.item_request_builder import ItemRequestBuilder
