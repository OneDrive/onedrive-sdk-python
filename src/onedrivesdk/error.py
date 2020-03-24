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
from __future__ import unicode_literals


class OneDriveError(Exception):

    def __init__(self, prop_dict, status_code):
        """Initialize a OneDriveError given the JSON
        error response dictionary, and the HTTP status code

        Args:
            prop_dict (dict): A dictionary containing the response
                from OneDrive
            status_code (int): The HTTP status code (ex. 200, 201, etc.)
        """
        if "code" not in prop_dict or "message" not in prop_dict:
            prop_dict["code"] = ErrorCode.Malformed
            prop_dict["message"] = "The received response was malformed"
            super(OneDriveError, self).__init__(prop_dict["code"]+" - "+prop_dict["message"])
        else:
            super(OneDriveError, self).__init__(prop_dict["code"]+" - "+prop_dict["message"])
        self._prop_dict = prop_dict
        self._status_code = status_code

    @property
    def status_code(self):
        """The HTTP status code

        Returns:
            int: The HTTP status code
        """
        return self._status_code

    @property
    def code(self):
        """The OneDrive error code sent back in
        the response. Possible codes can be found
        in the :class:`ErrorCode` enum.

        Returns:
            str: The error code
        """
        return self._prop_dict["code"]

    @property
    def inner_error(self):
        """Creates a OneDriveError object from the specified inner 
        error within the response.

        Returns:
            :class:`OneDriveError`: Error from within the inner
                response
        """
        return OneDriveError(self._prop_dict["innererror"], self.status_code) if "innererror" in self._prop_dict else None

    def matches(self, code):
        """Recursively searches the :class:`OneDriveError` to find
        if the specified code was found

        Args:
            code (str): The error code to search for

        Returns:
            bool: True if the error code was found, false otherwise
        """
        if self.code == code:
            return True

        return False if self.inner_error is None else self.inner_error.matches(code)


class ErrorCode(object):
    #: Access was denied to the resource
    AccessDenied = "accessDenied"
    #: The activity limit has been reached
    ActivityLimitReached = "activityLimitReached"
    #: A general exception occured
    GeneralException = "generalException"
    #: An invalid range was provided
    InvalidRange = "invalidRange"
    #: An invalid request was provided
    InvalidRequest = "invalidRequest"
    #: The requested resource was not found
    ItemNotFound = "itemNotFound"
    #: Malware was detected in the resource
    MalwareDetected = "malwareDetected"
    #: The name already exists
    NameAlreadyExists = "nameAlreadyExists"
    #: The action was not allowed
    NotAllowed = "notAllowed"
    #: The action was not supported
    NotSupported = "notSupported"
    #: The resource was modified
    ResourceModified = "resourceModified"
    #: A resync is required
    ResyncRequired = "resyncRequired"
    #: The OneDrive service is not available
    ServiceNotAvailable = "serviceNotAvailable"
    #: The quota for this OneDrive has been reached
    QuotaLimitReached = "quotaLimitReached"
    #: The user is unauthenticated
    Unauthenticated = "unauthenticated"

    #: The response was malformed
    Malformed = "malformed"

    #: Path exceeds maximum length.
    PathIsTooLong = 'pathIsTooLong'
    #: Name contains invalid characters.
    InvalidPath = 'invalidPath'
    #: Folder hierarchy depth limit reached.
    PathTooDeep = 'pathTooDeep'
    #: Too many requests.
    ThrottledRequest = 'throttledRequest'
