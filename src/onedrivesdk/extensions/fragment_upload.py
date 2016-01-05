# -*- coding: utf-8 -*-
'''
------------------------------------------------------------------------------
 Copyright (c) 2015 Microsoft Corporation

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
------------------------------------------------------------------------------
'''

from ..error import OneDriveError
from ..model.upload_session import UploadSession
from ..options import HeaderOption
from ..request.item_request_builder import ItemRequestBuilder
from ..request_builder_base import RequestBuilderBase
from ..request_base import RequestBase
from ..helpers.file_slice import FileSlice
import asyncio
import json
import math
import os
import time

__PART_SIZE = 10 * 1024 * 1024 # recommended file size. Should be multiple of 320 * 1024
__MAX_SINGLE_FILE_UPLOAD = 100 * 1024 * 1024

class ItemUploadFragment(RequestBase):
    def __init__(self, request_url, client, options, file_handle):
        super(ItemUploadFragment, self).__init__(request_url, client, options)
        self.method = "PUT"
        self._file_handle = file_handle

    def post(self):
        """Sends the POST request

        Returns:
            :class:`UploadSession<onedrivesdk.model.upload_session.UploadSession>`:
                The resulting entity from the operation
        """
        entity = UploadSession(json.loads(self.send(data=self._file_handle).content))
        return entity

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine

        Yields:
            :class:`UploadedSession<onedrivesdk.model.upload_session.UploadedSession>`:
                The resulting entity from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.post)
        entity = yield from future
        return entity

class ItemUploadFragmentBuilder(RequestBuilderBase):
    def __init__(self, request_url, client, content_local_path):
        super(ItemUploadFragmentBuilder, self).__init__(request_url, client)
        self._method_options = {}
        self._file_handle = open(content_local_path, "rb")
        self._total_length = os.stat(content_local_path).st_size

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._file_handle.close()

    def request(self, begin, length, options=None):
        """Builds the request for the ItemUploadFragment

        Args:
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                Default to None, list of options to include in the request

        Returns:
            :class:`ItemUploadFragment<onedrivesdk.request.item_upload_fragment.ItemUploadFragment>`:
                The request
        """
        opts = None
        if not (options is None or len(options) == 0):
            opts = options.copy()
        else:
            opts = []

        self.content_type = "application/octet-stream"

        opts.append(HeaderOption("Content-Range", "bytes %d-%d/%d" % (begin, begin + length - 1, self._total_length)))
        opts.append(HeaderOption("Content-Length", length))

        file_slice = FileSlice(self._file_handle, begin, length=length)
        req = ItemUploadFragment(self._request_url, self._client, opts, file_slice)
        return req

    def post(self, begin, length, options=None):
        """Sends the POST request

        Returns:
            :class:`UploadedFragment<onedrivesdk.model.uploaded_fragment.UploadedFragment>`:
            The resulting UploadSession from the operation
        """
        return self.request(begin, length, options).post()

    @asyncio.coroutine
    def post_async(self, begin, length, options=None):
        """Sends the POST request using an asyncio coroutine

        Yields:
            :class:`UploadedFragment<onedrivesdk.model.uploaded_fragment.UploadedFragment>`:
                The resulting UploadSession from the operation
        """
        entity = yield from self.request(begin, length, options).post_async()
        return entity


def fragment_upload(self, local_path, upload_status=None):
    """Uploads file using PUT using multipart upload if needed.

    Args:
        local_path (str): The path to the local file to upload.
        upload_status (func): function(current_part, total_parts) to be called
            with upload status for each 10MB part

    Returns:
        Created entity.
    """
    file_size = os.stat(local_path).st_size
    if file_size <= __MAX_SINGLE_FILE_UPLOAD:
        # fallback to single shot upload if file is small enough
        return self.content.request().upload(local_path)
    else:
        # multipart upload needed for larger files
        session = self.create_session().post()

        with ItemUploadFragmentBuilder(session.upload_url, self._client, local_path) as upload_builder:
            total_parts = math.ceil(file_size / __PART_SIZE)
            for i in range(total_parts):
                if upload_status:
                    upload_status(i, total_parts)

                length = min(__PART_SIZE, file_size - i  * __PART_SIZE)
                tries = 0
                while True:
                    try:
                        tries += 1
                        resp = upload_builder.post(i * __PART_SIZE, length)
                    except OneDriveError as exc:
                        if exc.status_code in (500, 502, 503, 504) and tries < 5:
                            time.sleep(5)
                            continue
                        elif exc.status_code == 401:
                            self._client.auth_provider.refresh_token()
                            continue
                        else:
                            raise exc
                    break # while True
        if upload_status:
            upload_status(total_parts, total_parts) # job completed
        # return last response
        return resp

ItemRequestBuilder.fragment_upload = fragment_upload
