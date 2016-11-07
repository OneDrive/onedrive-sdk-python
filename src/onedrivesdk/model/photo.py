# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Photo(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

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
        self._prop_dict["takenDateTime"] = val.isoformat()+((".0" if val.time().microsecond == 0 else "")+"Z")

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

