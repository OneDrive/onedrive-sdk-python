# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from ..request_base import RequestBase
from ..model.subscription import Subscription
import json
import asyncio

class SubscriptionRequest(RequestBase):
    """The type SubscriptionRequest."""
    
    def __init__(self, request_url, client, options):
        """Constructs a new SubscriptionRequest.

        Args:
            request_url (str): The url to perform the SubscriptionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(SubscriptionRequest, self).__init__(request_url, client, options)

    def delete(self):
        """Deletes the specified Subscription."""
        self.method = "DELETE"
        self.send()

    async def delete_async(self):
        """Deletes the specified Subscription."""
        future = self._client._loop.run_in_executor(None,
                                                    self.delete)
        await future

    def get(self):
        """Gets the specified Subscription.
        
        Returns:
            :class:`Subscription<onedrivesdk.model.subscription.Subscription>`:
                The Subscription.
        """
        self.method = "GET"
        entity = Subscription(json.loads(self.send().content))
        self._initialize_collection_properties(entity)
        return entity

    async def get_async(self):
        """Gets the specified Subscription in async.

        Yields:
            :class:`Subscription<onedrivesdk.model.subscription.Subscription>`:
                The Subscription.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        entity = await future
        return entity

    def update(self, subscription):
        """Updates the specified Subscription.
        
        Args:
            subscription (:class:`Subscription<onedrivesdk.model.subscription.Subscription>`):
                The Subscription to update.

        Returns:
            :class:`Subscription<onedrivesdk.model.subscription.Subscription>`:
                The updated Subscription.
        """
        self.content_type = "application/json"
        self.method = "PATCH"
        entity = Subscription(json.loads(self.send(subscription).content))
        self._initialize_collection_properties(entity)
        return entity

    async def update_async(self, subscription):
        """Updates the specified Subscription in async
        
        Args:
            subscription (:class:`Subscription<onedrivesdk.model.subscription.Subscription>`):
                The Subscription to update.

        Yields:
            :class:`Subscription<onedrivesdk.model.subscription.Subscription>`:
                The updated Subscription.
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.update,
                                                    subscription)
        entity = await future
        return entity

