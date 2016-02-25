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
from ..model.identity import Identity
from ..one_drive_object_base import OneDriveObjectBase


class IdentitySet(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
