# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class UploadSession(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def upload_url(self):
        """Gets and sets the uploadUrl
        
        Returns: 
            str:
                The uploadUrl
        """
        if "uploadUrl" in self._prop_dict:
            return self._prop_dict["uploadUrl"]
        else:
            return None

    @upload_url.setter
    def upload_url(self, val):
        self._prop_dict["uploadUrl"] = val

    @property
    def expiration_date_time(self):
        """Gets and sets the expirationDateTime
        
        Returns: 
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+((".0" if val.time().microsecond == 0 else "")+"Z")

    @property
    def next_expected_ranges(self):
        """Gets and sets the nextExpectedRanges
        
        Returns: 
            str:
                The nextExpectedRanges
        """
        if "nextExpectedRanges" in self._prop_dict:
            return self._prop_dict["nextExpectedRanges"]
        else:
            return None

    @next_expected_ranges.setter
    def next_expected_ranges(self, val):
        self._prop_dict["nextExpectedRanges"] = val

