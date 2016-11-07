# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.hashes import Hashes
from ..one_drive_object_base import OneDriveObjectBase


class File(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict is not None else {}

    @property
    def hashes(self):
        """
        Gets and sets the hashes
        
        Returns: 
            :class:`Hashes<onedrivesdk.model.hashes.Hashes>`:
                The hashes
        """
        if "hashes" in self._prop_dict:
            if isinstance(self._prop_dict["hashes"], OneDriveObjectBase):
                return self._prop_dict["hashes"]
            else :
                self._prop_dict["hashes"] = Hashes(self._prop_dict["hashes"])
                return self._prop_dict["hashes"]

        return None

    @hashes.setter
    def hashes(self, val):
        self._prop_dict["hashes"] = val
    @property
    def mime_type(self):
        """Gets and sets the mimeType
        
        Returns: 
            str:
                The mimeType
        """
        if "mimeType" in self._prop_dict:
            return self._prop_dict["mimeType"]
        else:
            return None

    @mime_type.setter
    def mime_type(self, val):
        self._prop_dict["mimeType"] = val

