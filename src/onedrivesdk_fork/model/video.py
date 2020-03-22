# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Video(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict is not None else {}

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

