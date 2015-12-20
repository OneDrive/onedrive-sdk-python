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

from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..model.item import Item
import json


class ItemContentRequest(RequestBase):
    def __init__(self, request_url, client, options):
        """Initialize the ItemContentRequest

        Args:
            request_url (str): The url to perform the ItemContentRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(ItemContentRequest, self).__init__(request_url, client, options)

    def upload(self, content_local_path):
        """Uploads the file using PUT
        
        Args:
            content_local_path (str):
                The path to the local file to upload.

        Returns: 
            :class:`Item<onedrivesdk.model.item.Item>`:
                The created Item.
        """
        file_size = os.stat(content_local_path).st_size
        if file_size <= 100 * 1024 * 1024:
            self.method = "PUT"
            entity_response = self.send(path=content_local_path)
            entity = Item(json.loads(entity_response.content))
            return entity
        else:
            # resumable upload needed for larger files
            session = ItemRequestBuilder(self._request, self._client).create_session()
            __PART_SIZE = 60 * 1024 * 1024

            with ItemUploadFragmentBuilder(session.uploadUrl, self._client, content_local_path) as upload_builder:
                for i in range(math.ceil(file_size / __PART_SIZE)):
                    resp = upload_builder.post(i * __PART_SIZE, __PART_SIZE)
            return resp

    def download(self, content_local_path):
        """Downloads the specified Item.
        
        Args:
            content_local_path (str):
                The path where the Item should be downloaded to
        """
        self.download_item(content_local_path)


class ItemContentRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ItemContentRequestBuilder
        
        Args:
            request_url (str): The request URL to initialize
                the ItemContentRequestBuilder at
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client to use for requests made by the
                ItemContentRequestBuilder
        """
        super(ItemContentRequestBuilder, self).__init__(request_url, client)

    def request(self):
        """Builds the ItemContentRequest

        Returns:
            :class:`ItemContentRequest<onedrivesdk.request.item_content.ItemContentRequest>`:
                The ItemContentRequest
        """
        return ItemContentRequest(self._request_url, self._client, None)
