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


class Video(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bitrate(self):
        """Gets and sets the bitrate
        
        Returns: 
            int:
                The bitrate
        """
        if "bitrate" in self._prop_dict:
            return self._prop_dict["bitrate"]
        else:
            return None

    @bitrate.setter
    def bitrate(self, val):
        self._prop_dict["bitrate"] = val

    @property
    def duration(self):
        """Gets and sets the duration
        
        Returns: 
            int:
                The duration
        """
        if "duration" in self._prop_dict:
            return self._prop_dict["duration"]
        else:
            return None

    @duration.setter
    def duration(self, val):
        self._prop_dict["duration"] = val

    @property
    def height(self):
        """Gets and sets the height
        
        Returns: 
            int:
                The height
        """
        if "height" in self._prop_dict:
            return self._prop_dict["height"]
        else:
            return None

    @height.setter
    def height(self, val):
        self._prop_dict["height"] = val

    @property
    def width(self):
        """Gets and sets the width
        
        Returns: 
            int:
                The width
        """
        if "width" in self._prop_dict:
            return self._prop_dict["width"]
        else:
            return None

    @width.setter
    def width(self, val):
        self._prop_dict["width"] = val

