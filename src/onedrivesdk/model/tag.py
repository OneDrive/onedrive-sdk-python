# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.auto_tagged import AutoTagged
from ..one_drive_object_base import OneDriveObjectBase


class Tag(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def auto_tagged(self):
        """
        Gets and sets the autoTagged
        
        Returns: 
            :class:`AutoTagged<onedrivesdk.model.auto_tagged.AutoTagged>`:
                The autoTagged
        """
        if "autoTagged" in self._prop_dict:
            if isinstance(self._prop_dict["autoTagged"], OneDriveObjectBase):
                return self._prop_dict["autoTagged"]
            else :
                self._prop_dict["autoTagged"] = AutoTagged(self._prop_dict["autoTagged"])
                return self._prop_dict["autoTagged"]

        return None

    @auto_tagged.setter
    def auto_tagged(self, val):
        self._prop_dict["autoTagged"] = val

    @property
    def name(self):
        """
        Gets and sets the name
        
        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

