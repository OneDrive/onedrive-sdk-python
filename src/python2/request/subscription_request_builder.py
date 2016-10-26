# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from .subscription_request import SubscriptionRequest
from ..request_builder_base import RequestBuilderBase


class SubscriptionRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the SubscriptionRequestBuilder

        Args:
            request_url (str): The url to perform the SubscriptionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
        """
        super(SubscriptionRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the SubscriptionRequest

        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`SubscriptionRequest<onedrivesdk.request.subscription_request.SubscriptionRequest>`:
                The SubscriptionRequest
        """
        req = SubscriptionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Subscription."""
        self.request().delete()

    def get(self):
        """Gets the specified Subscription.
        
        Returns:
            :class:`Subscription<onedrivesdk.model.subscription.Subscription>`:
                The Subscription.
        """
        return self.request().get()

    def update(self, subscription):
        """Updates the specified Subscription.
        
        Args:
            subscription (:class:`Subscription<onedrivesdk.model.subscription.Subscription>`):
                The Subscription to update.

        Returns:
            :class:`Subscription<onedrivesdk.model.subscription.Subscription>`:
                The updated Subscription
        """
        return self.request().update(subscription)

