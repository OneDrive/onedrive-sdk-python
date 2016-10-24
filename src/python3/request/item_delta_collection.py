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
from ..model.item_delta_collection_page import ItemDeltaCollectionPage
from ..request.items_collection import ItemsCollectionResponse


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
        next_page_link = self._prop_dict["@odata.nextLink"] if "@odata.nextLink" in self._prop_dict else None

        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
            self._collection_page._token = token
            self._collection_page._delta_link = delta_link
            self._collection_page._next_page_link = next_page_link
        else:
            self._collection_page = ItemDeltaCollectionPage(self._prop_dict["value"],
                                                            token,
                                                            delta_link,
                                                            next_page_link)

        return self._collection_page

from ..request.item_delta import ItemDeltaRequest