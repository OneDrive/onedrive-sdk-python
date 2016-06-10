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
            if value.items and value.items._prop_dict:
                if "items@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["items@odata.nextLink"]
                    value.items._init_next_page_request(next_page_link, self._client, None)
            if value.shared and value.shared._prop_dict:
                if "shared@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["shared@odata.nextLink"]
                    value.shared._init_next_page_request(next_page_link, self._client, None)
            if value.special and value.special._prop_dict:
                if "special@odata.nextLink" in value._prop_dict:
                    next_page_link = value._prop_dict["special@odata.nextLink"]
                    value.special._init_next_page_request(next_page_link, self._client, None)
