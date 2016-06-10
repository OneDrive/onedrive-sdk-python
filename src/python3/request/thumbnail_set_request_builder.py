# -*- coding: utf-8 -*- 
'''
# Copyright (c) 2015 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from .thumbnail_set_request import ThumbnailSetRequest
from ..request_builder_base import RequestBuilderBase
from ..request.thumbnail_request_builder import ThumbnailRequestBuilder
import asyncio


class ThumbnailSetRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ThumbnailSetRequestBuilder

        Args:
            request_url (str): The url to perform the ThumbnailSetRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
        """
        super(ThumbnailSetRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ThumbnailSetRequest

        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ThumbnailSetRequest<onedrivesdk.request.thumbnail_set_request.ThumbnailSetRequest>`:
                The ThumbnailSetRequest
        """
        req = ThumbnailSetRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified ThumbnailSet."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified ThumbnailSet."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified ThumbnailSet.
        
        Returns:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The ThumbnailSet.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified ThumbnailSet in async.

        Returns:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The ThumbnailSet.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, thumbnail_set):
        """Updates the specified ThumbnailSet.
        
        Args:
            thumbnail_set (:class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`):
                The ThumbnailSet to update.

        Returns:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The updated ThumbnailSet
        """
        return self.request().update(thumbnail_set)

    @asyncio.coroutine
    def update_async(self, thumbnail_set):
        """Updates the specified ThumbnailSet in async
        
        Args:
            thumbnail_set (:class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`):
                The ThumbnailSet to update.

        Returns:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The updated ThumbnailSet.
        """
        entity = yield from self.request().update_async(thumbnail_set)
        return entity

    @property
    def large(self):
        """The large for the ThumbnailSetRequestBuilder

        Returns: 
            :class:`ThumbnailRequestBuilder<onedrivesdk.request.thumbnail_request.ThumbnailRequestBuilder>`:
                A request builder created from the ThumbnailSetRequestBuilder
        """
        return ThumbnailRequestBuilder(self.append_to_request_url("large"), self._client)

    @property
    def medium(self):
        """The medium for the ThumbnailSetRequestBuilder

        Returns: 
            :class:`ThumbnailRequestBuilder<onedrivesdk.request.thumbnail_request.ThumbnailRequestBuilder>`:
                A request builder created from the ThumbnailSetRequestBuilder
        """
        return ThumbnailRequestBuilder(self.append_to_request_url("medium"), self._client)

    @property
    def small(self):
        """The small for the ThumbnailSetRequestBuilder

        Returns: 
            :class:`ThumbnailRequestBuilder<onedrivesdk.request.thumbnail_request.ThumbnailRequestBuilder>`:
                A request builder created from the ThumbnailSetRequestBuilder
        """
        return ThumbnailRequestBuilder(self.append_to_request_url("small"), self._client)

    @property
    def source(self):
        """The source for the ThumbnailSetRequestBuilder

        Returns: 
            :class:`ThumbnailRequestBuilder<onedrivesdk.request.thumbnail_request.ThumbnailRequestBuilder>`:
                A request builder created from the ThumbnailSetRequestBuilder
        """
        return ThumbnailRequestBuilder(self.append_to_request_url("source"), self._client)
