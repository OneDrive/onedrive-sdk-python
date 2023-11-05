# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..model.permission import Permission
from ..collection_base import CollectionRequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
import asyncio


class ItemInviteRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options, recipients, require_sign_in=None, roles=None, send_invitation=None, message=None):
        super(ItemInviteRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if recipients:
            self.body_options["recipients"] = recipients
        if require_sign_in:
            self.body_options["requireSignIn"] = require_sign_in
        if roles:
            self.body_options["roles"] = roles
        if send_invitation:
            self.body_options["sendInvitation"] = send_invitation
        if message:
            self.body_options["message"] = message

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`ItemsCollectionResponse<onedrivesdk.request.items_collection.ItemsCollectionResponse>`:
                The resulting collection page from the operation
        """
        self.content_type = "application/json"
        collection_response = ItemsCollectionResponse(json.loads(self.send(self.body_options).content))
        return self._page_from_response(collection_response)

    async def post_async(self):
        """Sends the POST request using an asyncio coroutine

        Yields:
            :class:`ItemsCollectionResponse<onedrivesdk.request.items_collection.ItemsCollectionResponse>`:
                The resulting collection page from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.post)
        collection_response = yield from future
        return collection_response


class ItemInviteRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, recipients, require_sign_in=None, roles=None, send_invitation=None, message=None):
        super(ItemInviteRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["recipients"] = recipients._prop_dict
        self._method_options["requireSignIn"] = require_sign_in
        self._method_options["roles"] = roles
        self._method_options["sendInvitation"] = send_invitation
        self._method_options["message"] = message

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the request for the ItemInvite
        
        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-seperated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`ItemInviteRequest<onedrivesdk.request.item_invite.ItemInviteRequest>`:
                The request
        """
        req = ItemInviteRequest(self._request_url, self._client, options, self._method_options["recipients"], require_sign_in=self._method_options["requireSignIn"], roles=self._method_options["roles"], send_invitation=self._method_options["sendInvitation"], message=self._method_options["message"])
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`ItemsCollectionResponse<onedrivesdk.request.items_collection.ItemsCollectionResponse>`:
            The resulting ItemsCollectionResponse from the operation
        """
        return self.request().post()

    async def post_async(self):
        """Sends the POST request using an asyncio coroutine
        
        Yields:
            :class:`ItemsCollectionResponse<onedrivesdk.request.items_collection.ItemsCollectionResponse>`:
                The resulting ItemsCollectionResponse from the operation
        """
        collection_page = yield from self.request().post_async()
        return collection_page

from ..request.items_collection import ItemsCollectionResponse
