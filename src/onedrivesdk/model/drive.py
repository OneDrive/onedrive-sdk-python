# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.quota import Quota
from ..model.status import Status
from ..model.item import Item
from ..one_drive_object_base import OneDriveObjectBase


class Drive(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

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
    def drive_type(self):
        """
        Gets and sets the driveType
        
        Returns:
            str:
                The driveType
        """
        if "driveType" in self._prop_dict:
            return self._prop_dict["driveType"]
        else:
            return None

    @drive_type.setter
    def drive_type(self, val):
        self._prop_dict["driveType"] = val

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
    def quota(self):
        """
        Gets and sets the quota
        
        Returns: 
            :class:`Quota<onedrivesdk.model.quota.Quota>`:
                The quota
        """
        if "quota" in self._prop_dict:
            if isinstance(self._prop_dict["quota"], OneDriveObjectBase):
                return self._prop_dict["quota"]
            else :
                self._prop_dict["quota"] = Quota(self._prop_dict["quota"])
                return self._prop_dict["quota"]

        return None

    @quota.setter
    def quota(self, val):
        self._prop_dict["quota"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`Status<onedrivesdk.model.status.Status>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = Status(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def items(self):
        """Gets and sets the items
        
        Returns: 
            :class:`ItemsCollectionPage<onedrivesdk.request.items_collection.ItemsCollectionPage>`:
                The items
        """
        if "items" in self._prop_dict:
            return ItemsCollectionPage(self._prop_dict["items"])
        else:
            return None

    @property
    def shared(self):
        """Gets and sets the shared
        
        Returns: 
            :class:`SharedCollectionPage<onedrivesdk.request.shared_collection.SharedCollectionPage>`:
                The shared
        """
        if "shared" in self._prop_dict:
            return SharedCollectionPage(self._prop_dict["shared"])
        else:
            return None

    @property
    def special(self):
        """Gets and sets the special
        
        Returns: 
            :class:`SpecialCollectionPage<onedrivesdk.request.special_collection.SpecialCollectionPage>`:
                The special
        """
        if "special" in self._prop_dict:
            return SpecialCollectionPage(self._prop_dict["special"])
        else:
            return None

from ..model.items_collection_page import ItemsCollectionPage
from ..model.shared_collection_page import SharedCollectionPage
from ..model.special_collection_page import SpecialCollectionPage
