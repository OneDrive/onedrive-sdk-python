# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.storage_plans import StoragePlans
from ..one_drive_object_base import OneDriveObjectBase


class Quota(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict is not None else {}

    @property
    def deleted(self):
        """Gets and sets the deleted
        
        Returns: 
            int:
                The deleted
        """
        if "deleted" in self._prop_dict:
            return self._prop_dict["deleted"]
        else:
            return None

    @deleted.setter
    def deleted(self, val):
        self._prop_dict["deleted"] = val

    @property
    def remaining(self):
        """Gets and sets the remaining
        
        Returns: 
            int:
                The remaining
        """
        if "remaining" in self._prop_dict:
            return self._prop_dict["remaining"]
        else:
            return None

    @remaining.setter
    def remaining(self, val):
        self._prop_dict["remaining"] = val

    @property
    def state(self):
        """Gets and sets the state
        
        Returns: 
            str:
                The state
        """
        if "state" in self._prop_dict:
            return self._prop_dict["state"]
        else:
            return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def total(self):
        """Gets and sets the total
        
        Returns: 
            int:
                The total
        """
        if "total" in self._prop_dict:
            return self._prop_dict["total"]
        else:
            return None

    @total.setter
    def total(self, val):
        self._prop_dict["total"] = val

    @property
    def used(self):
        """Gets and sets the used
        
        Returns: 
            int:
                The used
        """
        if "used" in self._prop_dict:
            return self._prop_dict["used"]
        else:
            return None

    @used.setter
    def used(self, val):
        self._prop_dict["used"] = val

    @property
    def storage_plans(self):
        """
        Gets and sets the storagePlans
        
        Returns: 
            :class:`StoragePlans<onedrivesdk.model.storage_plans.StoragePlans>`:
                The storagePlans
        """
        if "storagePlans" in self._prop_dict:
            if isinstance(self._prop_dict["storagePlans"], OneDriveObjectBase):
                return self._prop_dict["storagePlans"]
            else :
                self._prop_dict["storagePlans"] = StoragePlans(self._prop_dict["storagePlans"])
                return self._prop_dict["storagePlans"]

        return None

    @storage_plans.setter
    def storage_plans(self, val):
        self._prop_dict["storagePlans"] = val
