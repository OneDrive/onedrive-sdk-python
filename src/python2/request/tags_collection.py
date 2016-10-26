# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase
from ..request_builder_base import RequestBuilderBase
from ..model.tags_collection_page import TagsCollectionPage
import json

class TagsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the TagsCollectionRequest
        
        Args:
            request_url (str): The url to perform the TagsCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(TagsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the TagsCollectionPage

        Returns: 
            :class:`TagsCollectionPage<onedrivesdk.model.tags_collection_page.TagsCollectionPage>`:
                The TagsCollectionPage
        """
        self.method = "GET"
        collection_response = TagsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


    @staticmethod
    def get_next_page_request(collection_page, client, options=None):
        """Gets the TagsCollectionRequest for the next page. Returns None if there is no next page

        Args:
            collection_page (:class:`TagsCollectionPage<onedrivesdk.model.tags_collection_page.TagsCollectionPage>`):
                The collection to get the next page for
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Yields: 
            :class:`TagsCollectionRequest<onedrivesdk.request.tags_collection.TagsCollectionRequest>`:
                The TagsCollectionRequest
        """
        if collection_page._next_page_link:
            return TagsCollectionRequest(collection_page._next_page_link, client, options)
        else:
            return None

class TagsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the TagRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a TagRequestBuilder for
        
        Returns: 
            :class:`TagRequestBuilder<onedrivesdk.request.tag_request_builder.TagRequestBuilder>`:
                A TagRequestBuilder for that key
        """
        return TagRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the TagsCollectionRequest
        
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
            :class:`TagsCollectionRequest<onedrivesdk.request.tags_collection.TagsCollectionRequest>`:
                The TagsCollectionRequest
        """
        req = TagsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the TagsCollectionPage

        Returns: 
            :class:`TagsCollectionPage<onedrivesdk.model.tags_collection_page.TagsCollectionPage>`:
                The TagsCollectionPage
        """
        return self.request().get()



class TagsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`TagsCollectionPage<onedrivesdk.model.tags_collection_page.TagsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = TagsCollectionPage(self._prop_dict["value"])

        return self._collection_page


from ..request.tag_request_builder import TagRequestBuilder
