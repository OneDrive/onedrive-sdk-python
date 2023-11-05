# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from .tag_request import TagRequest
from ..request_builder_base import RequestBuilderBase
import asyncio


class TagRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the TagRequestBuilder

        Args:
            request_url (str): The url to perform the TagRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
        """
        super(TagRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the TagRequest

        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`TagRequest<onedrivesdk.request.tag_request.TagRequest>`:
                The TagRequest
        """
        req = TagRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Tag."""
        self.request().delete()

    async def delete_async(self):
        """Deletes the specified Tag."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Tag.
        
        Returns:
            :class:`Tag<onedrivesdk.model.tag.Tag>`:
                The Tag.
        """
        return self.request().get()

    async def get_async(self):
        """Gets the specified Tag in async.

        Returns:
            :class:`Tag<onedrivesdk.model.tag.Tag>`:
                The Tag.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, tag):
        """Updates the specified Tag.
        
        Args:
            tag (:class:`Tag<onedrivesdk.model.tag.Tag>`):
                The Tag to update.

        Returns:
            :class:`Tag<onedrivesdk.model.tag.Tag>`:
                The updated Tag
        """
        return self.request().update(tag)

    async def update_async(self, tag):
        """Updates the specified Tag in async
        
        Args:
            tag (:class:`Tag<onedrivesdk.model.tag.Tag>`):
                The Tag to update.

        Returns:
            :class:`Tag<onedrivesdk.model.tag.Tag>`:
                The updated Tag.
        """
        entity = yield from self.request().update_async(tag)
        return entity
