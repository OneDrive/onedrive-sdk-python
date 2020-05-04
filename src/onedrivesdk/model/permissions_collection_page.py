# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionPageBase
from ..model.permission import Permission


class PermissionsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Permission at the index specified
        
        Args:
            index (int): The index of the item to get from the PermissionsCollectionPage

        Returns:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The Permission at the index
        """
        return Permission(self._prop_list[index])

    def permissions(self):
        """Get a generator of Permission within the PermissionsCollectionPage
        
        Yields:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The next Permission in the collection
        """
        for item in self._prop_list:
            yield Permission(item)
