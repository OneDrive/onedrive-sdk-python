# -*- coding: utf-8 -*- 
'''
# Copyright (c) 2015 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.open_with_app import OpenWithApp
from ..one_drive_object_base import OneDriveObjectBase


class OpenWithSet(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def web_embedded(self):
        """
        Gets and sets the webEmbedded
        
        Returns: 
            :class:`OpenWithApp<onedrivesdk.model.open_with_app.OpenWithApp>`:
                The webEmbedded
        """
        if "webEmbedded" in self._prop_dict:
            if isinstance(self._prop_dict["webEmbedded"], OneDriveObjectBase):
                return self._prop_dict["webEmbedded"]
            else :
                self._prop_dict["webEmbedded"] = OpenWithApp(self._prop_dict["webEmbedded"])
                return self._prop_dict["webEmbedded"]

        return None

    @web_embedded.setter
    def web_embedded(self, val):
        self._prop_dict["webEmbedded"] = val
