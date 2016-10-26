# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionPageBase
from ..model.tag import Tag


class TagsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Tag at the index specified
        
        Args:
            index (int): The index of the item to get from the TagsCollectionPage

        Returns:
            :class:`Tag<onedrivesdk.model.tag.Tag>`:
                The Tag at the index
        """
        return Tag(self._prop_list[index])

    def tags(self):
        """Get a generator of Tag within the TagsCollectionPage
        
        Yields:
            :class:`Tag<onedrivesdk.model.tag.Tag>`:
                The next Tag in the collection
        """
        for item in self._prop_list:
            yield Tag(item)
