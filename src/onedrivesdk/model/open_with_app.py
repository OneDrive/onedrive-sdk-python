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
from ..model.identity import Identity
from ..one_drive_object_base import OneDriveObjectBase


class OpenWithApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app(self):
        """
        Gets and sets the app
        
        Returns: 
            :class:`Identity<onedrivesdk.model.identity.Identity>`:
                The app
        """
        if "app" in self._prop_dict:
            if isinstance(self._prop_dict["app"], OneDriveObjectBase):
                return self._prop_dict["app"]
            else :
                self._prop_dict["app"] = Identity(self._prop_dict["app"])
                return self._prop_dict["app"]

        return None

    @app.setter
    def app(self, val):
        self._prop_dict["app"] = val
    @property
    def view_url(self):
        """Gets and sets the viewUrl
        
        Returns: 
            str:
                The viewUrl
        """
        if "viewUrl" in self._prop_dict:
            return self._prop_dict["viewUrl"]
        else:
            return None

    @view_url.setter
    def view_url(self, val):
        self._prop_dict["viewUrl"] = val

    @property
    def edit_url(self):
        """Gets and sets the editUrl
        
        Returns: 
            str:
                The editUrl
        """
        if "editUrl" in self._prop_dict:
            return self._prop_dict["editUrl"]
        else:
            return None

    @edit_url.setter
    def edit_url(self, val):
        self._prop_dict["editUrl"] = val

    @property
    def post_parameters(self):
        """Gets and sets the postParameters
        
        Returns: 
            str:
                The postParameters
        """
        if "postParameters" in self._prop_dict:
            return self._prop_dict["postParameters"]
        else:
            return None

    @post_parameters.setter
    def post_parameters(self, val):
        self._prop_dict["postParameters"] = val

