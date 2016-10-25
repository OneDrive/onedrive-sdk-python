# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionPageBase
from ..model.item import Item


class ItemsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Item at the index specified
        
        Args:
            index (int): The index of the item to get from the ItemsCollectionPage

        Returns:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item at the index
        """
        return Item(self._prop_list[index])

    def items(self):
        """Get a generator of Item within the ItemsCollectionPage
        
        Yields:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The next Item in the collection
        """
        for item in self._prop_list:
            yield Item(item)
