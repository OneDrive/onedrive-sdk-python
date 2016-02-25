# -*- coding: utf-8 -*- 
'''
# Copyright (c) 2015 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Location(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def altitude(self):
        """Gets and sets the altitude
        
        Returns: 
            float:
                The altitude
        """
        if "altitude" in self._prop_dict:
            return self._prop_dict["altitude"]
        else:
            return None

    @altitude.setter
    def altitude(self, val):
        self._prop_dict["altitude"] = val

    @property
    def latitude(self):
        """Gets and sets the latitude
        
        Returns: 
            float:
                The latitude
        """
        if "latitude" in self._prop_dict:
            return self._prop_dict["latitude"]
        else:
            return None

    @latitude.setter
    def latitude(self, val):
        self._prop_dict["latitude"] = val

    @property
    def longitude(self):
        """Gets and sets the longitude
        
        Returns: 
            float:
                The longitude
        """
        if "longitude" in self._prop_dict:
            return self._prop_dict["longitude"]
        else:
            return None

    @longitude.setter
    def longitude(self, val):
        self._prop_dict["longitude"] = val

