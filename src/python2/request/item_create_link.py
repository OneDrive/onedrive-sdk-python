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

from ..model.permission import Permission
from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json


class ItemCreateLinkRequest(RequestBase):

    def __init__(self, request_url, client, options, type):
        super(ItemCreateLinkRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if type:
            self.body_options["type"] = type

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The resulting entity from the operation
        """
        self.content_type = "application/json"
        entity = Permission(json.loads(self.send(self.body_options).content))
        return entity



class ItemCreateLinkRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, type):
        super(ItemCreateLinkRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["type"] = type

    def request(self, options=None):
        """Builds the request for the ItemCreateLink
        
        Args:
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`ItemCreateLinkRequest<onedrivesdk.request.item_create_link.ItemCreateLinkRequest>`:
                The request
        """
        req = ItemCreateLinkRequest(self._request_url, self._client, options, self._method_options["type"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
            The resulting Permission from the operation
        """
        return self.request().post()

