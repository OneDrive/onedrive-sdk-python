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
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Photo(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def camera_make(self):
        """Gets and sets the cameraMake
        
        Returns: 
            str:
                The cameraMake
        """
        if "cameraMake" in self._prop_dict:
            return self._prop_dict["cameraMake"]
        else:
            return None

    @camera_make.setter
    def camera_make(self, val):
        self._prop_dict["cameraMake"] = val

    @property
    def camera_model(self):
        """Gets and sets the cameraModel
        
        Returns: 
            str:
                The cameraModel
        """
        if "cameraModel" in self._prop_dict:
            return self._prop_dict["cameraModel"]
        else:
            return None

    @camera_model.setter
    def camera_model(self, val):
        self._prop_dict["cameraModel"] = val

    @property
    def exposure_denominator(self):
        """Gets and sets the exposureDenominator
        
        Returns: 
            float:
                The exposureDenominator
        """
        if "exposureDenominator" in self._prop_dict:
            return self._prop_dict["exposureDenominator"]
        else:
            return None

    @exposure_denominator.setter
    def exposure_denominator(self, val):
        self._prop_dict["exposureDenominator"] = val

    @property
    def exposure_numerator(self):
        """Gets and sets the exposureNumerator
        
        Returns: 
            float:
                The exposureNumerator
        """
        if "exposureNumerator" in self._prop_dict:
            return self._prop_dict["exposureNumerator"]
        else:
            return None

    @exposure_numerator.setter
    def exposure_numerator(self, val):
        self._prop_dict["exposureNumerator"] = val

    @property
    def focal_length(self):
        """Gets and sets the focalLength
        
        Returns: 
            float:
                The focalLength
        """
        if "focalLength" in self._prop_dict:
            return self._prop_dict["focalLength"]
        else:
            return None

    @focal_length.setter
    def focal_length(self, val):
        self._prop_dict["focalLength"] = val

    @property
    def f_number(self):
        """Gets and sets the fNumber
        
        Returns: 
            float:
                The fNumber
        """
        if "fNumber" in self._prop_dict:
            return self._prop_dict["fNumber"]
        else:
            return None

    @f_number.setter
    def f_number(self, val):
        self._prop_dict["fNumber"] = val

    @property
    def taken_date_time(self):
        """Gets and sets the takenDateTime
        
        Returns: 
            datetime:
                The takenDateTime
        """
        if "takenDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["takenDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @taken_date_time.setter
    def taken_date_time(self, val):
        self._prop_dict["takenDateTime"] = val.isoformat()+"Z"

    @property
    def iso(self):
        """Gets and sets the iso
        
        Returns: 
            int:
                The iso
        """
        if "iso" in self._prop_dict:
            return self._prop_dict["iso"]
        else:
            return None

    @iso.setter
    def iso(self, val):
        self._prop_dict["iso"] = val

