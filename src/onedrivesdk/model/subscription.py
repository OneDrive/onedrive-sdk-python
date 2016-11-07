# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Subscription(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def app_type(self):
        """
        Gets and sets the appType
        
        Returns:
            str:
                The appType
        """
        if "appType" in self._prop_dict:
            return self._prop_dict["appType"]
        else:
            return None

    @app_type.setter
    def app_type(self, val):
        self._prop_dict["appType"] = val

    @property
    def client_state(self):
        """
        Gets and sets the clientState
        
        Returns:
            str:
                The clientState
        """
        if "clientState" in self._prop_dict:
            return self._prop_dict["clientState"]
        else:
            return None

    @client_state.setter
    def client_state(self, val):
        self._prop_dict["clientState"] = val

    @property
    def created_by(self):
        """
        Gets and sets the createdBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], OneDriveObjectBase):
                return self._prop_dict["createdBy"]
            else :
                self._prop_dict["createdBy"] = IdentitySet(self._prop_dict["createdBy"])
                return self._prop_dict["createdBy"]

        return None

    @created_by.setter
    def created_by(self, val):
        self._prop_dict["createdBy"] = val

    @property
    def expiration_date_time(self):
        """
        Gets and sets the expirationDateTime
        
        Returns:
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+((".0" if val.time().microsecond == 0 else "")+"Z")

    @property
    def id(self):
        """
        Gets and sets the id
        
        Returns:
            str:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

    @property
    def muted(self):
        """
        Gets and sets the muted
        
        Returns:
            bool:
                The muted
        """
        if "muted" in self._prop_dict:
            return self._prop_dict["muted"]
        else:
            return None

    @muted.setter
    def muted(self, val):
        self._prop_dict["muted"] = val

    @property
    def notification_url(self):
        """
        Gets and sets the notificationUrl
        
        Returns:
            str:
                The notificationUrl
        """
        if "notificationUrl" in self._prop_dict:
            return self._prop_dict["notificationUrl"]
        else:
            return None

    @notification_url.setter
    def notification_url(self, val):
        self._prop_dict["notificationUrl"] = val

    @property
    def resource(self):
        """
        Gets and sets the resource
        
        Returns:
            str:
                The resource
        """
        if "resource" in self._prop_dict:
            return self._prop_dict["resource"]
        else:
            return None

    @resource.setter
    def resource(self, val):
        self._prop_dict["resource"] = val

    @property
    def scenarios(self):
        """
        Gets and sets the scenarios
        
        Returns:
            str:
                The scenarios
        """
        if "scenarios" in self._prop_dict:
            return self._prop_dict["scenarios"]
        else:
            return None

    @scenarios.setter
    def scenarios(self, val):
        self._prop_dict["scenarios"] = val

