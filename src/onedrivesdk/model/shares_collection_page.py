# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionPageBase
from ..model.share import Share


class SharesCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Share at the index specified
        
        Args:
            index (int): The index of the item to get from the SharesCollectionPage

        Returns:
            :class:`Share<onedrivesdk.model.share.Share>`:
                The Share at the index
        """
        return Share(self._prop_list[index])

    def shares(self):
        """Get a generator of Share within the SharesCollectionPage
        
        Yields:
            :class:`Share<onedrivesdk.model.share.Share>`:
                The next Share in the collection
        """
        for item in self._prop_list:
            yield Share(item)
