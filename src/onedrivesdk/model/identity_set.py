# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity import Identity
from ..one_drive_object_base import OneDriveObjectBase


class IdentitySet(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def application(self):
        """
        Gets and sets the application
        
        Returns: 
            :class:`Identity<onedrivesdk.model.identity.Identity>`:
                The application
        """
        if "application" in self._prop_dict:
            if isinstance(self._prop_dict["application"], OneDriveObjectBase):
                return self._prop_dict["application"]
            else :
                self._prop_dict["application"] = Identity(self._prop_dict["application"])
                return self._prop_dict["application"]

        return None

    @application.setter
    def application(self, val):
        self._prop_dict["application"] = val
    @property
    def device(self):
        """
        Gets and sets the device
        
        Returns: 
            :class:`Identity<onedrivesdk.model.identity.Identity>`:
                The device
        """
        if "device" in self._prop_dict:
            if isinstance(self._prop_dict["device"], OneDriveObjectBase):
                return self._prop_dict["device"]
            else :
                self._prop_dict["device"] = Identity(self._prop_dict["device"])
                return self._prop_dict["device"]

        return None

    @device.setter
    def device(self, val):
        self._prop_dict["device"] = val
    @property
    def user(self):
        """
        Gets and sets the user
        
        Returns: 
            :class:`Identity<onedrivesdk.model.identity.Identity>`:
                The user
        """
        if "user" in self._prop_dict:
            if isinstance(self._prop_dict["user"], OneDriveObjectBase):
                return self._prop_dict["user"]
            else :
                self._prop_dict["user"] = Identity(self._prop_dict["user"])
                return self._prop_dict["user"]

        return None

    @user.setter
    def user(self, val):
        self._prop_dict["user"] = val
