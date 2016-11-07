# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.open_with_app import OpenWithApp
from ..one_drive_object_base import OneDriveObjectBase


class OpenWithSet(OneDriveObjectBase):

    def __init__(self, prop_dict=None):
        self._prop_dict = prop_dict if prop_dict else {}

    @property
    def web(self):
        """
        Gets and sets the web
        
        Returns: 
            :class:`OpenWithApp<onedrivesdk.model.open_with_app.OpenWithApp>`:
                The web
        """
        if "web" in self._prop_dict:
            if isinstance(self._prop_dict["web"], OneDriveObjectBase):
                return self._prop_dict["web"]
            else :
                self._prop_dict["web"] = OpenWithApp(self._prop_dict["web"])
                return self._prop_dict["web"]

        return None

    @web.setter
    def web(self, val):
        self._prop_dict["web"] = val
    @property
    def web_embed(self):
        """
        Gets and sets the webEmbed
        
        Returns: 
            :class:`OpenWithApp<onedrivesdk.model.open_with_app.OpenWithApp>`:
                The webEmbed
        """
        if "webEmbed" in self._prop_dict:
            if isinstance(self._prop_dict["webEmbed"], OneDriveObjectBase):
                return self._prop_dict["webEmbed"]
            else :
                self._prop_dict["webEmbed"] = OpenWithApp(self._prop_dict["webEmbed"])
                return self._prop_dict["webEmbed"]

        return None

    @web_embed.setter
    def web_embed(self, val):
        self._prop_dict["webEmbed"] = val
