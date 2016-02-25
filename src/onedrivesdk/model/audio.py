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
from ..one_drive_object_base import OneDriveObjectBase


class Audio(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def album(self):
        """Gets and sets the album
        
        Returns: 
            str:
                The album
        """
        if "album" in self._prop_dict:
            return self._prop_dict["album"]
        else:
            return None

    @album.setter
    def album(self, val):
        self._prop_dict["album"] = val

    @property
    def album_artist(self):
        """Gets and sets the albumArtist
        
        Returns: 
            str:
                The albumArtist
        """
        if "albumArtist" in self._prop_dict:
            return self._prop_dict["albumArtist"]
        else:
            return None

    @album_artist.setter
    def album_artist(self, val):
        self._prop_dict["albumArtist"] = val

    @property
    def artist(self):
        """Gets and sets the artist
        
        Returns: 
            str:
                The artist
        """
        if "artist" in self._prop_dict:
            return self._prop_dict["artist"]
        else:
            return None

    @artist.setter
    def artist(self, val):
        self._prop_dict["artist"] = val

    @property
    def bitrate(self):
        """Gets and sets the bitrate
        
        Returns: 
            int:
                The bitrate
        """
        if "bitrate" in self._prop_dict:
            return self._prop_dict["bitrate"]
        else:
            return None

    @bitrate.setter
    def bitrate(self, val):
        self._prop_dict["bitrate"] = val

    @property
    def composers(self):
        """Gets and sets the composers
        
        Returns: 
            str:
                The composers
        """
        if "composers" in self._prop_dict:
            return self._prop_dict["composers"]
        else:
            return None

    @composers.setter
    def composers(self, val):
        self._prop_dict["composers"] = val

    @property
    def copyright(self):
        """Gets and sets the copyright
        
        Returns: 
            str:
                The copyright
        """
        if "copyright" in self._prop_dict:
            return self._prop_dict["copyright"]
        else:
            return None

    @copyright.setter
    def copyright(self, val):
        self._prop_dict["copyright"] = val

    @property
    def disc(self):
        """Gets and sets the disc
        
        Returns: 
            int:
                The disc
        """
        if "disc" in self._prop_dict:
            return self._prop_dict["disc"]
        else:
            return None

    @disc.setter
    def disc(self, val):
        self._prop_dict["disc"] = val

    @property
    def disc_count(self):
        """Gets and sets the discCount
        
        Returns: 
            int:
                The discCount
        """
        if "discCount" in self._prop_dict:
            return self._prop_dict["discCount"]
        else:
            return None

    @disc_count.setter
    def disc_count(self, val):
        self._prop_dict["discCount"] = val

    @property
    def duration(self):
        """Gets and sets the duration
        
        Returns: 
            int:
                The duration
        """
        if "duration" in self._prop_dict:
            return self._prop_dict["duration"]
        else:
            return None

    @duration.setter
    def duration(self, val):
        self._prop_dict["duration"] = val

    @property
    def genre(self):
        """Gets and sets the genre
        
        Returns: 
            str:
                The genre
        """
        if "genre" in self._prop_dict:
            return self._prop_dict["genre"]
        else:
            return None

    @genre.setter
    def genre(self, val):
        self._prop_dict["genre"] = val

    @property
    def has_drm(self):
        """Gets and sets the hasDrm
        
        Returns: 
            bool:
                The hasDrm
        """
        if "hasDrm" in self._prop_dict:
            return self._prop_dict["hasDrm"]
        else:
            return None

    @has_drm.setter
    def has_drm(self, val):
        self._prop_dict["hasDrm"] = val

    @property
    def is_variable_bitrate(self):
        """Gets and sets the isVariableBitrate
        
        Returns: 
            bool:
                The isVariableBitrate
        """
        if "isVariableBitrate" in self._prop_dict:
            return self._prop_dict["isVariableBitrate"]
        else:
            return None

    @is_variable_bitrate.setter
    def is_variable_bitrate(self, val):
        self._prop_dict["isVariableBitrate"] = val

    @property
    def title(self):
        """Gets and sets the title
        
        Returns: 
            str:
                The title
        """
        if "title" in self._prop_dict:
            return self._prop_dict["title"]
        else:
            return None

    @title.setter
    def title(self, val):
        self._prop_dict["title"] = val

    @property
    def track(self):
        """Gets and sets the track
        
        Returns: 
            int:
                The track
        """
        if "track" in self._prop_dict:
            return self._prop_dict["track"]
        else:
            return None

    @track.setter
    def track(self, val):
        self._prop_dict["track"] = val

    @property
    def track_count(self):
        """Gets and sets the trackCount
        
        Returns: 
            int:
                The trackCount
        """
        if "trackCount" in self._prop_dict:
            return self._prop_dict["trackCount"]
        else:
            return None

    @track_count.setter
    def track_count(self, val):
        self._prop_dict["trackCount"] = val

    @property
    def year(self):
        """Gets and sets the year
        
        Returns: 
            int:
                The year
        """
        if "year" in self._prop_dict:
            return self._prop_dict["year"]
        else:
            return None

    @year.setter
    def year(self, val):
        self._prop_dict["year"] = val

