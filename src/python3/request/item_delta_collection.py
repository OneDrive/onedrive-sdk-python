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
from ..request.items_collection import ItemsCollectionResponse, ItemsCollectionPage


class ItemDeltaCollectionResponse(ItemsCollectionResponse):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ItemDeltaCollectionPage<onedrivesdk.request.item_delta_collection.ItemDeltaCollectionPage>`:
                The collection page
        """
        token = self._prop_dict["@delta.token"] if "@delta.token" in self._prop_dict else None
        delta_link = self._prop_dict["@odata.deltaLink"] if "@odata.deltaLink" in self._prop_dict else None

        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
            self._collection_page._token = token
            self._collection_page._delta_link = delta_link
        else:
            self._collection_page = ItemDeltaCollectionPage(self._prop_dict["value"],
                                                            token,
                                                            delta_link)

        return self._collection_page

class ItemDeltaCollectionPage(ItemsCollectionPage):

    def __init__(self, prop_list, token=None, delta_link=None):
        super(ItemDeltaCollectionPage, self).__init__(prop_list)
        self._token = token
        self._delta_link = delta_link

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ItemDeltaCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`OneDriveClient<onedrivesdk.model.one_drive_client.OneDriveClient>`:
                The client to be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`:
                A list of options
        """
        self._next_page_request = ItemDeltaRequest(next_page_link, client, options)

    @property
    def token(self):
        """Gets the token property from the
        ItemDeltaCollectionPage

        Returns:
            str:
                The token property from the ItemDeltaCollectionPage
        """
        return self._token

    @property
    def delta_link(self):
        """Gets the deltaLink property from the
        ItemDeltaCollectionPage

        Returns:
            str:
                The deltaLink property from the ItemDeltaCollectionPage
        """
        return self._delta_link

from ..request.item_delta import ItemDeltaRequest