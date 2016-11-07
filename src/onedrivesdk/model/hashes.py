# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Hashes(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def crc32_hash(self):
        """Gets and sets the crc32Hash
        
        Returns: 
            str:
                The crc32Hash
        """
        if "crc32Hash" in self._prop_dict:
            return self._prop_dict["crc32Hash"]
        else:
            return None

    @crc32_hash.setter
    def crc32_hash(self, val):
        self._prop_dict["crc32Hash"] = val

    @property
    def sha1_hash(self):
        """Gets and sets the sha1Hash
        
        Returns: 
            str:
                The sha1Hash
        """
        if "sha1Hash" in self._prop_dict:
            return self._prop_dict["sha1Hash"]
        else:
            return None

    @sha1_hash.setter
    def sha1_hash(self, val):
        self._prop_dict["sha1Hash"] = val

