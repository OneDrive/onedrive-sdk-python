# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..one_drive_object_base import OneDriveObjectBase


class Shared(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def effective_roles(self):
        """Gets and sets the effectiveRoles
        
        Returns: 
            str:
                The effectiveRoles
        """
        if "effectiveRoles" in self._prop_dict:
            return self._prop_dict["effectiveRoles"]
        else:
            return None

    @effective_roles.setter
    def effective_roles(self, val):
        self._prop_dict["effectiveRoles"] = val

    @property
    def owner(self):
        """
        Gets and sets the owner
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The owner
        """
        if "owner" in self._prop_dict:
            if isinstance(self._prop_dict["owner"], OneDriveObjectBase):
                return self._prop_dict["owner"]
            else :
                self._prop_dict["owner"] = IdentitySet(self._prop_dict["owner"])
                return self._prop_dict["owner"]

        return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val
    @property
    def scope(self):
        """Gets and sets the scope
        
        Returns: 
            str:
                The scope
        """
        if "scope" in self._prop_dict:
            return self._prop_dict["scope"]
        else:
            return None

    @scope.setter
    def scope(self, val):
        self._prop_dict["scope"] = val

