# -*- coding: utf-8 -*- 
'''
# Copyright (c) 2015 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from .thumbnail_request import ThumbnailRequest
from ..request_builder_base import RequestBuilderBase
from ..request.thumbnail_content_request import ThumbnailContentRequestBuilder
import asyncio


class ThumbnailRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ThumbnailRequestBuilder

        Args:
            request_url (str): The url to perform the ThumbnailRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
        """
        super(ThumbnailRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ThumbnailRequest

        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ThumbnailRequest<onedrivesdk.request.thumbnail_request.ThumbnailRequest>`:
                The ThumbnailRequest
        """
        req = ThumbnailRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Thumbnail."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Thumbnail."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Thumbnail.
        
        Returns:
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The Thumbnail.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Thumbnail in async.

        Returns:
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The Thumbnail.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, thumbnail):
        """Updates the specified Thumbnail.
        
        Args:
            thumbnail (:class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`):
                The Thumbnail to update.

        Returns:
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The updated Thumbnail
        """
        return self.request().update(thumbnail)

    @asyncio.coroutine
    def update_async(self, thumbnail):
        """Updates the specified Thumbnail in async
        
        Args:
            thumbnail (:class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`):
                The Thumbnail to update.

        Returns:
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The updated Thumbnail.
        """
        entity = yield from self.request().update_async(thumbnail)
        return entity

    def download(self, local_path):
        """Downloads the specified entity.

        Args:
            local_path (str): The path where the entity should be
                downloaded to
        """
        return self.content.request().download(local_path)

    @asyncio.coroutine
    def download_async(self, local_path):
        """Downloads the specified entity in async.

        Args:
            local_path (str): The path where the entity should be
                downloaded to
        """
        entity = yield from self.content.request().download_async(local_path)
        return entity

    @property
    def content(self):
        """The content for the ThumbnailRequestBuilder

        Returns: 
            :class:`ThumbnailContentRequestBuilder<onedrivesdk.request.thumbnail_content.ThumbnailContentRequestBuilder>`:
                A request builder created from the ThumbnailRequestBuilder
        """
        return ThumbnailContentRequestBuilder(self.append_to_request_url("content"), self._client)
