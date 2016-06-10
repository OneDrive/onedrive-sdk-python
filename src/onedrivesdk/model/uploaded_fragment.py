# -*- coding: utf-8 -*- 
'''
# The MIT License (MIT)
# Copyright (c) 2015 Wiktor Niesiobedzki
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
# 
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class UploadedFragment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
        self._prop_dict["expirationDateTime"] = val.isoformat()+"Z"

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

    @property
    def id(self):
        """Gets and sets id

        Returns:
            str: item id
        """
        return self._prop_dict.get("id")

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val
    
    @property
    def name(self):
        """Gets and sets file name

        Returns:
            str: file name
        """
        return self._prop_dict.get("name")

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def size(self):
        """Gets and sets file size

        Returns:
            str: file size
        """
        return self._prop_dict.get("size")

    @size.setter
    def size(self, val):
        self._prop_dict["size"] = val

    @property
    def file(self):
        """Gets and sets file dictionary

        Returns:
            dict: dictionary of fils
        """
        self._prop_dict.get("file")

    @file.setter
    def file(self, val):
        self._prop_dict["file"] = val
