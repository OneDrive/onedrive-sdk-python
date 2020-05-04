# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionPageBase
from ..model.subscription import Subscription


class SubscriptionsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Subscription at the index specified
        
        Args:
            index (int): The index of the item to get from the SubscriptionsCollectionPage

        Returns:
            :class:`Subscription<onedrivesdk.model.subscription.Subscription>`:
                The Subscription at the index
        """
        return Subscription(self._prop_list[index])

    def subscriptions(self):
        """Get a generator of Subscription within the SubscriptionsCollectionPage
        
        Yields:
            :class:`Subscription<onedrivesdk.model.subscription.Subscription>`:
                The next Subscription in the collection
        """
        for item in self._prop_list:
            yield Subscription(item)
