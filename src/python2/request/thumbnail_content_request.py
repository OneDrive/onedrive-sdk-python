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
from ..request_builder_base import RequestBuilderBase
from ..model.thumbnail import Thumbnail
import json


class ThumbnailContentRequest(RequestBase):
    def __init__(self, request_url, client, options):
        """Initialize the ThumbnailContentRequest

        Args:
            request_url (str): The url to perform the ThumbnailContentRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(ThumbnailContentRequest, self).__init__(request_url, client, options)

    def download(self, content_local_path):
        """Downloads the specified Thumbnail.
        
        Args:
            content_local_path (str):
                The path where the Thumbnail should be downloaded to
        """
        self.download_item(content_local_path)


class ThumbnailContentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ThumbnailContentRequestBuilder
        
        Args:
            request_url (str): The request URL to initialize
                the ThumbnailContentRequestBuilder at
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client to use for requests made by the
                ThumbnailContentRequestBuilder
        """
        super(ThumbnailContentRequestBuilder, self).__init__(request_url, client)

    def request(self):
        """Builds the ThumbnailContentRequest

        Returns:
            :class:`ThumbnailContentRequest<onedrivesdk.request.thumbnail_content.ThumbnailContentRequest>`:
                The ThumbnailContentRequest
        """
        return ThumbnailContentRequest(self._request_url, self._client, None)