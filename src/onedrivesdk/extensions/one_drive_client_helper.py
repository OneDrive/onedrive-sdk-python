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
from ..request.one_drive_client import OneDriveClient
from ..request.drive_request_builder import DriveRequestBuilder


def item(self, drive=None, id=None, path=None):
    """Gets an item given the specified (optional) drive,
    (optional) id, and (optional) path

    Args:
        drive (str): The drive that you want to use
        id (str): The id of the item to request
        path (str): The path of the item to request

    Returns:
        :class:`ItemRequestBuilder<onedrivesdk.requests.item_request_builder.ItemRequestBuilder>`:
            A request builder for an item given a path or id
    """
    if id is None and path is None:
        raise ValueError("Either 'path' or 'id' must be specified")
    elif id is not None and path is not None:
        raise ValueError("Only one of either 'path' or 'id' can be specified")

    drive_builder = self.drives[drive] if drive else self.drive

    if path:
        return drive_builder.item_by_path(path)
    elif id:
        return drive_builder.items[id]


@property
def drive(self):
    """Gets the user's default drive

    Returns: 
        :class:`DriveRequestBuilder<onedrivesdk.requests.drive_request_builder.DriveRequestBuilder>`:
            User's default drive
    """
    return DriveRequestBuilder(self.base_url + "drive", self)

OneDriveClient.item = item
OneDriveClient.drive = drive
