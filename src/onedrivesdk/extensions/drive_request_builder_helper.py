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

from ..request.drive_request_builder import DriveRequestBuilder
from ..request.item_request_builder import ItemRequestBuilder


def item_by_path(self, path):
    """Get an item by path in OneDrive
    
    Args
        path (str): The path to the requested item

    Returns: 
        :class:`ItemRequestBuilder<onedrivesdk.requests.item_request_builder.ItemRequestBuilder>`:
            A request builder for an item given a path
    """
    #strip any leading '/'
    path = str(path)[1:] if str(path)[0] == "/" else str(path)
    return ItemRequestBuilder(self.append_to_request_url("root:/"+str(path)+":"), self._client)

DriveRequestBuilder.item_by_path = item_by_path
