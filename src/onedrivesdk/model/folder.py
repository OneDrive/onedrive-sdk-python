# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Folder(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def child_count(self):
        """Gets and sets the childCount
        
        Returns: 
            int:
                The childCount
        """
        if "childCount" in self._prop_dict:
            return self._prop_dict["childCount"]
        else:
            return None

    @child_count.setter
    def child_count(self, val):
        self._prop_dict["childCount"] = val

