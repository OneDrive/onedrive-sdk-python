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
from __future__ import with_statement
from .model.async_operation_status import AsyncOperationStatus
from .model.item import Item
from .request_base import RequestBase
import threading
import json


class AsyncOperationMonitor(RequestBase):

    def __init__(self, request_url, client, options):
        """Initializes the AsyncOperationMonitor

        Args:
            request_url (str): The request URL to ping for the
                :class:`AsyncOperationStatus<onedrivesdk.models.async_operation_status.AsyncOperationStatus>`
            client (:class:`OneDriveClient<onedrivesdk.requests.one_drive_client.OneDriveClient>`): 
                The client to use for the requests
            options (list): A list of 
                :class:`Option<onedrivesdk.options.Option>`
                to send with the request
        """
        super(AsyncOperationMonitor, self).__init__(request_url,
                                                    client,
                                                    options)
        self._lock = threading.Lock()
        self.method = "GET"
        self._completed = False
        self._has_errors = False
        self._item = None
        self._status = None

        self._start_poll_on_thread()

    def _start_poll_on_thread(self):
        """Begins the polling on a seperate thread"""
        t = threading.Thread(target=self._polling_loop)
        t.start()

    def _stop_poll_on_thread(self):
        """Stops polling on a seperate thread"""
        self.completed = True

    def _polling_loop(self):
        """This method to run within a new thread (as to not block).
        This method will send requests to the status URL until
        the operation has completed (or failed). The AsyncOperationStatus
        will update on each poll. Upon completion, the item (or errors)
        will be populated.
        """
        while not self.completed:
            response = self.send()
            if response.content:
                response_dict = json.loads(response.content)

                with self._lock:
                    self._status_code = response.status

                    if "status" not in response_dict:
                        self._completed = True
                    else:
                        self._status = AsyncOperationStatus(response_dict)
                        if self._status.status == AsyncOperationStatusType.Failed or self._status.status == AsyncOperationStatusType.DeleteFailed:
                            self._completed = True
                            self._has_errors = True

                    if self._completed:
                        self._item = None if self._has_errors else Item(response_dict)

    def poll_until_done(self):
        """Method blocks until done polling for the result 
        of the async operation is returned

        Returns:
            :class:`Item<onedrivesdk.models.item.Item>`: 
                The item from the async operation
        """
        while not self.completed:
            pass
        return self.item

    @property
    def status(self):
        """The status of the async operation
        
        Returns:
            :class:`AsyncOperationStatus<onedrivesdk.models.async_operation_status.AsyncOperationStatus>`:
                The async operation status
        """
        with self._lock:
            return self._status

    @property
    def item(self):
        """Result of the async operation will be placed here when
        polling is completed

        Returns:
            :class:`Item<onedrivesdk.models.item.Item>`:
                The item from async operation
        """
        with self._lock:
            return self._item

    @property
    def completed(self):
        """Whether or not the async operation has completed

        Returns:
            bool: Whether or not the async operation has completed
        """
        with self._lock:
            return self._completed

    @property
    def has_errors(self):
        """Whether or not the async operation has errors
        
        Returns:
            bool: Whether or not the async operation has errors
        """
        with self._lock:
            return self._has_errors


class AsyncOperationStatusType(object):
    """Various status types that can be found in
    the :class:`onedrivesdk.models.async_operation_status.AsyncOperationStatus` status
    """

    #: The operation has not started yet
    NotStarted = "notStarted"
    #: The operation is in progress
    InProgress = "inProgress"
    #: The operation has completed
    Completed = "completed"
    #: The operation is updating
    Updating = "updating"
    #: The operation has failed
    Failed = "failed"
    #: The delete is pending
    DeletePending = "deletePending"
    #: The delete has failed
    DeleteFailed = "deleteFailed"
    #: The operation is waiting to start
    Waiting = "waiting"
