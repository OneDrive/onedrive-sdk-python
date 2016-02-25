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
from ..model.identity_set import IdentitySet
from ..model.item import Item
from ..one_drive_object_base import OneDriveObjectBase


class Share(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def name(self):
        """
        Gets and sets the name
        
        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

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

