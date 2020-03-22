'''
------------------------------------------------------------------------------
 Copyright (c) 2015 Microsoft Corporation

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
------------------------------------------------------------------------------
'''
from datetime import datetime

class OneDriveObjectBase(object):

    DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
    DATETIME_FORMAT_NO_MILLISECONDS = "%Y-%m-%dT%H:%M:%SZ"
    
    def to_dict(self):
        """Returns the serialized form of the :class:`OneDriveObjectBase`
        as a dict. All sub-objects that are based off of :class:`OneDriveObjectBase`
        are also serialized and inserted into the dict
        
        Returns:
            dict: The serialized form of the :class:`OneDriveObjectBase`
        """
        serialized = {}

        for prop in self._prop_dict:
            if isinstance(self._prop_dict[prop], OneDriveObjectBase):
                serialized[prop] = self._prop_dict[prop].to_dict()
            else:
                serialized[prop] = self._prop_dict[prop]

        return serialized
        
    @staticmethod
    def get_datetime_from_string(s):
        try:
            dt = datetime.strptime(
                s,
                OneDriveObjectBase.DATETIME_FORMAT)
        except ValueError as ve:
            # Try again with other format
            dt = datetime.strptime(
                s,
                OneDriveObjectBase.DATETIME_FORMAT_NO_MILLISECONDS)
        return dt
        
    @staticmethod
    def get_string_from_datetime(dt):
        return dt.strftime(OneDriveObjectBase.DATETIME_FORMAT)
