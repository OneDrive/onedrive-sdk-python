# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Status(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict is not None else {}

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
    def lockdown_date_time(self):
        """Gets and sets the lockdownDateTime
        
        Returns: 
            datetime:
                The lockdownDateTime
        """
        if "lockdownDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lockdownDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @lockdown_date_time.setter
    def lockdown_date_time(self, val):
        self._prop_dict["lockdownDateTime"] = val.isoformat()+((".0" if val.time().microsecond == 0 else "")+"Z")

    @property
    def lockdown_reasons(self):
        """Gets and sets the lockdownReasons
        
        Returns: 
            str:
                The lockdownReasons
        """
        if "lockdownReasons" in self._prop_dict:
            return self._prop_dict["lockdownReasons"]
        else:
            return None

    @lockdown_reasons.setter
    def lockdown_reasons(self, val):
        self._prop_dict["lockdownReasons"] = val

    @property
    def drive_deletion_date_time(self):
        """Gets and sets the driveDeletionDateTime
        
        Returns: 
            datetime:
                The driveDeletionDateTime
        """
        if "driveDeletionDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["driveDeletionDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @drive_deletion_date_time.setter
    def drive_deletion_date_time(self, val):
        self._prop_dict["driveDeletionDateTime"] = val.isoformat()+((".0" if val.time().microsecond == 0 else "")+"Z")

    @property
    def last_unlock_date_time(self):
        """Gets and sets the lastUnlockDateTime
        
        Returns: 
            datetime:
                The lastUnlockDateTime
        """
        if "lastUnlockDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastUnlockDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_unlock_date_time.setter
    def last_unlock_date_time(self, val):
        self._prop_dict["lastUnlockDateTime"] = val.isoformat()+((".0" if val.time().microsecond == 0 else "")+"Z")

    @property
    def user_unlocks(self):
        """Gets and sets the userUnlocks
        
        Returns: 
            int:
                The userUnlocks
        """
        if "userUnlocks" in self._prop_dict:
            return self._prop_dict["userUnlocks"]
        else:
            return None

    @user_unlocks.setter
    def user_unlocks(self, val):
        self._prop_dict["userUnlocks"] = val

    @property
    def user_unlocks_remaining(self):
        """Gets and sets the userUnlocksRemaining
        
        Returns: 
            int:
                The userUnlocksRemaining
        """
        if "userUnlocksRemaining" in self._prop_dict:
            return self._prop_dict["userUnlocksRemaining"]
        else:
            return None

    @user_unlocks_remaining.setter
    def user_unlocks_remaining(self, val):
        self._prop_dict["userUnlocksRemaining"] = val

    @property
    def support_agent_unlocks(self):
        """Gets and sets the supportAgentUnlocks
        
        Returns: 
            int:
                The supportAgentUnlocks
        """
        if "supportAgentUnlocks" in self._prop_dict:
            return self._prop_dict["supportAgentUnlocks"]
        else:
            return None

    @support_agent_unlocks.setter
    def support_agent_unlocks(self, val):
        self._prop_dict["supportAgentUnlocks"] = val

