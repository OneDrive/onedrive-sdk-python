# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from .drive_request import DriveRequest
from ..request_builder_base import RequestBuilderBase
from ..request.drive_recent import DriveRecentRequestBuilder


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
    def recent(self):
        """Executes the recent method


        Returns:
            :class:`DriveRecentRequestBuilder<onedrivesdk.request.drive_recent.DriveRecentRequestBuilder>`:
                A DriveRecentRequestBuilder for the method
        """
        return DriveRecentRequestBuilder(self.append_to_request_url("recent"), self._client)

from ..request.items_collection import ItemsCollectionRequestBuilder
from ..request.shared_collection import SharedCollectionRequestBuilder
from ..request.special_collection import SpecialCollectionRequestBuilder
