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
from .permission_request import PermissionRequest
from ..request_builder_base import RequestBuilderBase


class PermissionRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the PermissionRequestBuilder

        Args:
            request_url (str): The url to perform the PermissionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
        """
        super(PermissionRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the PermissionRequest

        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`PermissionRequest<onedrivesdk.request.permission_request.PermissionRequest>`:
                The PermissionRequest
        """
        req = PermissionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Permission."""
        self.request().delete()

    def get(self):
        """Gets the specified Permission.
        
        Returns:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The Permission.
        """
        return self.request().get()

    def update(self, permission):
        """Updates the specified Permission.
        
        Args:
            permission (:class:`Permission<onedrivesdk.model.permission.Permission>`):
                The Permission to update.

        Returns:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The updated Permission
        """
        return self.request().update(permission)

