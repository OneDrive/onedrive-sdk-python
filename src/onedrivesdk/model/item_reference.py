# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class ItemReference(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict is not None else {}

    @property
    def drive_id(self):
        """Gets and sets the driveId
        
        Returns: 
            str:
                The driveId
        """
        if "driveId" in self._prop_dict:
            return self._prop_dict["driveId"]
        else:
            return None

    @drive_id.setter
    def drive_id(self, val):
        self._prop_dict["driveId"] = val

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
    def path(self):
        """Gets and sets the path
        
        Returns: 
            str:
                The path
        """
        if "path" in self._prop_dict:
            return self._prop_dict["path"]
        else:
            return None

    @path.setter
    def path(self, val):
        self._prop_dict["path"] = val

