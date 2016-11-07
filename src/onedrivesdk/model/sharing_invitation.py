# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..one_drive_object_base import OneDriveObjectBase


class SharingInvitation(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def email(self):
        """Gets and sets the email
        
        Returns: 
            str:
                The email
        """
        if "email" in self._prop_dict:
            return self._prop_dict["email"]
        else:
            return None

    @email.setter
    def email(self, val):
        self._prop_dict["email"] = val

    @property
    def invited_by(self):
        """
        Gets and sets the invitedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The invitedBy
        """
        if "invitedBy" in self._prop_dict:
            if isinstance(self._prop_dict["invitedBy"], OneDriveObjectBase):
                return self._prop_dict["invitedBy"]
            else :
                self._prop_dict["invitedBy"] = IdentitySet(self._prop_dict["invitedBy"])
                return self._prop_dict["invitedBy"]

        return None

    @invited_by.setter
    def invited_by(self, val):
        self._prop_dict["invitedBy"] = val
    @property
    def sign_in_required(self):
        """Gets and sets the signInRequired
        
        Returns: 
            bool:
                The signInRequired
        """
        if "signInRequired" in self._prop_dict:
            return self._prop_dict["signInRequired"]
        else:
            return None

    @sign_in_required.setter
    def sign_in_required(self, val):
        self._prop_dict["signInRequired"] = val

    @property
    def send_invitation_status(self):
        """Gets and sets the sendInvitationStatus
        
        Returns: 
            str:
                The sendInvitationStatus
        """
        if "sendInvitationStatus" in self._prop_dict:
            return self._prop_dict["sendInvitationStatus"]
        else:
            return None

    @send_invitation_status.setter
    def send_invitation_status(self, val):
        self._prop_dict["sendInvitationStatus"] = val

    @property
    def invite_error_resolve_url(self):
        """Gets and sets the inviteErrorResolveUrl
        
        Returns: 
            str:
                The inviteErrorResolveUrl
        """
        if "inviteErrorResolveUrl" in self._prop_dict:
            return self._prop_dict["inviteErrorResolveUrl"]
        else:
            return None

    @invite_error_resolve_url.setter
    def invite_error_resolve_url(self, val):
        self._prop_dict["inviteErrorResolveUrl"] = val

