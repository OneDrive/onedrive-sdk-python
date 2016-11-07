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
from ..model.items_collection_page import ItemsCollectionPage

class ItemDeltaCollectionPage(ItemsCollectionPage):

    def __init__(self, prop_list, token=None, delta_link=None, next_page_link=None):
        super(ItemDeltaCollectionPage, self).__init__(prop_list)
        self._next_page_link = next_page_link
        self._token = token
        self._delta_link = delta_link

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

    @property
    def next_page_link(self):
        """Gets the nextLink property from the
        ItemDeltaCollectionPage

        Returns:
            str:
                The nextLink property from the ItemDeltaCollectionPage
        """
        return self._delta_link