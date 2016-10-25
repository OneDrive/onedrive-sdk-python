# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..request_base import RequestBase
from ..model.drive import Drive
import json

class DriveRequest(RequestBase):
    """The type DriveRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new DriveRequest.

        Args:
            request_url (str): The url to perform the DriveRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(DriveRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Drive."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Drive.
        
        Returns:
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The Drive.
        """
        self.method = "GET"
        entity = Drive(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, drive):
        """Updates the specified Drive.
        
        Args:
            drive (:class:`Drive<onedrivesdk.model.drive.Drive>`):
                The Drive to update.

        Returns:
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The updated Drive.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Drive(json.loads(self.send(drive).content))
        self._initialize_collection_properties(entity)
        return entity

    def _initialize_collection_properties(self, value):
        if value and value._prop_dict:
            if value.items:
                if "items@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["items@odata.nextLink"]
                    value.items._next_page_link = next_page_link
            if value.shared:
                if "shared@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["shared@odata.nextLink"]
                    value.shared._next_page_link = next_page_link
            if value.special:
                if "special@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["special@odata.nextLink"]
                    value.special._next_page_link = next_page_link
