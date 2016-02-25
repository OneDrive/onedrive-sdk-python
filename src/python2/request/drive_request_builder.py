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
from .drive_request import DriveRequest
from ..request_builder_base import RequestBuilderBase


class DriveRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the DriveRequestBuilder

        Args:
            request_url (str): The url to perform the DriveRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
        """
        super(DriveRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the DriveRequest

        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`DriveRequest<onedrivesdk.request.drive_request.DriveRequest>`:
                The DriveRequest
        """
        req = DriveRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Drive."""
        self.request().delete()

    def get(self):
        """Gets the specified Drive.
        
        Returns:
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The Drive.
        """
        return self.request().get()

    def update(self, drive):
        """Updates the specified Drive.
        
        Args:
            drive (:class:`Drive<onedrivesdk.model.drive.Drive>`):
                The Drive to update.

        Returns:
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The updated Drive
        """
        return self.request().update(drive)


    @property
    def items(self):
        """The items for the DriveRequestBuilder

        Returns: 
            :class:`ItemsCollectionRequestBuilder<onedrivesdk.request.items_collection.ItemsCollectionRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return ItemsCollectionRequestBuilder(self.append_to_request_url("items"), self._client)

    @property
    def shared(self):
        """The shared for the DriveRequestBuilder

        Returns: 
            :class:`SharedCollectionRequestBuilder<onedrivesdk.request.shared_collection.SharedCollectionRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return SharedCollectionRequestBuilder(self.append_to_request_url("shared"), self._client)

    @property
    def special(self):
        """The special for the DriveRequestBuilder

        Returns: 
            :class:`SpecialCollectionRequestBuilder<onedrivesdk.request.special_collection.SpecialCollectionRequestBuilder>`:
                A request builder created from the DriveRequestBuilder
        """
        return SpecialCollectionRequestBuilder(self.append_to_request_url("special"), self._client)
from ..request.items_collection import ItemsCollectionRequestBuilder
from ..request.shared_collection import SharedCollectionRequestBuilder
from ..request.special_collection import SpecialCollectionRequestBuilder
