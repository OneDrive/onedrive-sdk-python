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
from ..model.thumbnail import Thumbnail
import json

class ThumbnailRequest(RequestBase):
    """The type ThumbnailRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new ThumbnailRequest.

        Args:
            request_url (str): The url to perform the ThumbnailRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(ThumbnailRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Thumbnail."""
        self.method = "DELETE"
        self.send()

    def get(self):
        """Gets the specified Thumbnail.
        
        Returns:
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The Thumbnail.
        """
        self.method = "GET"
        entity = Thumbnail(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    def update(self, thumbnail):
        """Updates the specified Thumbnail.
        
        Args:
            thumbnail (:class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`):
                The Thumbnail to update.

        Returns:
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The updated Thumbnail.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Thumbnail(json.loads(self.send(thumbnail).content))
        self._initialize_collection_properties(entity)
        return entity

