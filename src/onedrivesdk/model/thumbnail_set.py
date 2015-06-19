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
from ..model.thumbnail import Thumbnail
from ..one_drive_object_base import OneDriveObjectBase


class ThumbnailSet(OneDriveObjectBase):

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
    def large(self):
        """
        Gets and sets the large
        
        Returns: 
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The large
        """
        if "large" in self._prop_dict:
            if isinstance(self._prop_dict["large"], OneDriveObjectBase):
                return self._prop_dict["large"]
            else :
                self._prop_dict["large"] = Thumbnail(self._prop_dict["large"])
                return self._prop_dict["large"]

        return None

    @large.setter
    def large(self, val):
        self._prop_dict["large"] = val

    @property
    def medium(self):
        """
        Gets and sets the medium
        
        Returns: 
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The medium
        """
        if "medium" in self._prop_dict:
            if isinstance(self._prop_dict["medium"], OneDriveObjectBase):
                return self._prop_dict["medium"]
            else :
                self._prop_dict["medium"] = Thumbnail(self._prop_dict["medium"])
                return self._prop_dict["medium"]

        return None

    @medium.setter
    def medium(self, val):
        self._prop_dict["medium"] = val

    @property
    def small(self):
        """
        Gets and sets the small
        
        Returns: 
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The small
        """
        if "small" in self._prop_dict:
            if isinstance(self._prop_dict["small"], OneDriveObjectBase):
                return self._prop_dict["small"]
            else :
                self._prop_dict["small"] = Thumbnail(self._prop_dict["small"])
                return self._prop_dict["small"]

        return None

    @small.setter
    def small(self, val):
        self._prop_dict["small"] = val

    @property
    def source(self):
        """
        Gets and sets the source
        
        Returns: 
            :class:`Thumbnail<onedrivesdk.model.thumbnail.Thumbnail>`:
                The source
        """
        if "source" in self._prop_dict:
            if isinstance(self._prop_dict["source"], OneDriveObjectBase):
                return self._prop_dict["source"]
            else :
                self._prop_dict["source"] = Thumbnail(self._prop_dict["source"])
                return self._prop_dict["source"]

        return None

    @source.setter
    def source(self, val):
        self._prop_dict["source"] = val

