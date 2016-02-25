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


class SharingLink(OneDriveObjectBase):

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
    def type(self):
        """Gets and sets the type
        
        Returns: 
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def web_url(self):
        """Gets and sets the webUrl
        
        Returns: 
            str:
                The webUrl
        """
        if "webUrl" in self._prop_dict:
            return self._prop_dict["webUrl"]
        else:
            return None

    @web_url.setter
    def web_url(self, val):
        self._prop_dict["webUrl"] = val

    @property
    def web_html(self):
        """Gets and sets the webHtml
        
        Returns: 
            str:
                The webHtml
        """
        if "webHtml" in self._prop_dict:
            return self._prop_dict["webHtml"]
        else:
            return None

    @web_html.setter
    def web_html(self, val):
        self._prop_dict["webHtml"] = val

    @property
    def configurator_url(self):
        """Gets and sets the configuratorUrl
        
        Returns: 
            str:
                The configuratorUrl
        """
        if "configuratorUrl" in self._prop_dict:
            return self._prop_dict["configuratorUrl"]
        else:
            return None

    @configurator_url.setter
    def configurator_url(self, val):
        self._prop_dict["configuratorUrl"] = val

