# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.thumbnail_set import ThumbnailSet
from ..one_drive_object_base import OneDriveObjectBase


class Identity(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict is not None else {}

    @property
    def display_name(self):
        """Gets and sets the displayName
        
        Returns: 
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def thumbnails(self):
        """
        Gets and sets the thumbnails
        
        Returns: 
            :class:`ThumbnailSet<onedrivesdk.model.thumbnail_set.ThumbnailSet>`:
                The thumbnails
        """
        if "thumbnails" in self._prop_dict:
            if isinstance(self._prop_dict["thumbnails"], OneDriveObjectBase):
                return self._prop_dict["thumbnails"]
            else :
                self._prop_dict["thumbnails"] = ThumbnailSet(self._prop_dict["thumbnails"])
                return self._prop_dict["thumbnails"]

        return None

    @thumbnails.setter
    def thumbnails(self, val):
        self._prop_dict["thumbnails"] = val
