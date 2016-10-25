# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionPageBase
from ..model.thumbnail_set import ThumbnailSet


class ThumbnailsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the ThumbnailSet at the index specified
        
        Args:
            index (int): The index of the item to get from the ThumbnailsCollectionPage

        Returns:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The ThumbnailSet at the index
        """
        return ThumbnailSet(self._prop_list[index])

    def thumbnails(self):
        """Get a generator of ThumbnailSet within the ThumbnailsCollectionPage
        
        Yields:
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The next ThumbnailSet in the collection
        """
        for item in self._prop_list:
            yield ThumbnailSet(item)
