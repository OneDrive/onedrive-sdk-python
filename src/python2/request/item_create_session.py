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

from ..model.upload_session import UploadSession
from ..request_base import RequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json


class ItemCreateSessionRequest(RequestBase):

    def __init__(self, request_url, client, options, item=None):
        super(ItemCreateSessionRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if item:
            self.body_options["item"] = item

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`UploadSession<onedrivesdk.model.upload_session.UploadSession>`:
                The resulting entity from the operation
        """
        self.content_type = "application/json"
        entity = UploadSession(json.loads(self.send(self.body_options).content))
        return entity



class ItemCreateSessionRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, item=None):
        super(ItemCreateSessionRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["item"] = item._prop_dict

    def request(self, options=None):
        """Builds the request for the ItemCreateSession
        
        Args:
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`ItemCreateSessionRequest<onedrivesdk.request.item_create_session.ItemCreateSessionRequest>`:
                The request
        """
        req = ItemCreateSessionRequest(self._request_url, self._client, options, item=self._method_options["item"])
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`UploadSession<onedrivesdk.model.upload_session.UploadSession>`:
            The resulting UploadSession from the operation
        """
        return self.request().post()

