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

from ..model.item import Item
from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..async_operation_monitor import AsyncOperationMonitor
from ..options import *
import json


class ItemCopyRequest(RequestBase):

    def __init__(self, request_url, client, options, name=None, parent_reference=None):
        super(ItemCopyRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if name:
            self.body_options["name"] = name
        if parent_reference:
            self.body_options["parentReference"] = parent_reference

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`AsyncOperationMonitor<onedrivesdk.async_operation_monitor.AsyncOperationMonitor>`:
                The resulting entity from the operation
        """
        self.content_type = "application/json"
        self.append_option(HeaderOption("Prefer", "respond-async"))
        response = self.send(self.body_options)
        entity = AsyncOperationMonitor(response.headers["Location"], self._client, None)
        return entity



class ItemCopyRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, name=None, parent_reference=None):
        super(ItemCopyRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["name"] = name
        self._method_options["parentReference"] = parent_reference._prop_dict

    def request(self, options=None):
        """Builds the request for the ItemCopy
        
        Args:
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`ItemCopyRequest<onedrivesdk.request.item_copy.ItemCopyRequest>`:
                The request
        """
        req = ItemCopyRequest(self._request_url, self._client, options, name=self._method_options["name"], parent_reference=self._method_options["parentReference"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`Item<onedrivesdk.model.item.Item>`:
            The resulting Item from the operation
        """
        return self.request().post()

