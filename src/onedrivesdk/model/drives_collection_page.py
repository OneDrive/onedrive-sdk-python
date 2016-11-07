# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionPageBase
from ..model.drive import Drive


class DrivesCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Drive at the index specified
        
        Args:
            index (int): The index of the item to get from the DrivesCollectionPage

        Returns:
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The Drive at the index
        """
        return Drive(self._prop_list[index])

    def drives(self):
        """Get a generator of Drive within the DrivesCollectionPage
        
        Yields:
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The next Drive in the collection
        """
        for item in self._prop_list:
            yield Drive(item)
