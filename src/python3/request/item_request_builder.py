# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from .item_request import ItemRequest
from ..request_builder_base import RequestBuilderBase
from ..request.item_create_session import ItemCreateSessionRequestBuilder
from ..request.item_copy import ItemCopyRequestBuilder
from ..request.item_create_link import ItemCreateLinkRequestBuilder
from ..request.item_invite import ItemInviteRequestBuilder
from ..request.item_delta import ItemDeltaRequestBuilder
from ..request.item_search import ItemSearchRequestBuilder
from ..request.item_content_request import ItemContentRequestBuilder
import asyncio


class ItemRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client):
        """Initialize the ItemRequestBuilder

        Args:
            request_url (str): The url to perform the ItemRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
        """
        super(ItemRequestBuilder, self).__init__(request_url, client)

    def request(self, expand=None, select=None, options=None):
        """Builds the ItemRequest

        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ItemRequest<onedrivesdk.request.item_request.ItemRequest>`:
                The ItemRequest
        """
        req = ItemRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select)
        return req

    def delete(self):
        """Deletes the specified Item."""
        self.request().delete()

    @asyncio.coroutine
    def delete_async(self):
        """Deletes the specified Item."""
        yield from self.request().delete_async()
    def get(self):
        """Gets the specified Item.
        
        Returns:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item.
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the specified Item in async.

        Returns:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The Item.
        """
        entity = yield from self.request().get_async()
        return entity
    def update(self, item):
        """Updates the specified Item.
        
        Args:
            item (:class:`Item<onedrivesdk.model.item.Item>`):
                The Item to update.

        Returns:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The updated Item
        """
        return self.request().update(item)

    @asyncio.coroutine
    def update_async(self, item):
        """Updates the specified Item in async
        
        Args:
            item (:class:`Item<onedrivesdk.model.item.Item>`):
                The Item to update.

        Returns:
            :class:`Item<onedrivesdk.model.item.Item>`:
                The updated Item.
        """
        entity = yield from self.request().update_async(item)
        return entity

    def upload(self, local_path):
        """Uploads the file using PUT
        
        Args:
            local_path (str): The path to the local file to upload.

        Returns: 
            The created entity.
        """
        return self.content.request().upload(local_path)
    def uploadFromData(self, data):
        """Uploads the file using PUT
        
        Args:
            local_path (str): The path to the local file to upload.

        Returns: 
            The created entity.
        """
        return self.content.request().uploadFromData(data)
    @asyncio.coroutine
    def upload_async(self, local_path):
        """Uploads the file using PUT in async
        
        Args:
            local_path (str): The path to the local file to upload.

        Returns: The created entity.
        """
        entity = yield from self.content.request().upload_async(local_path)
        return entity

    def download(self, local_path):
        """Downloads the specified entity.

        Args:
            local_path (str): The path where the entity should be
                downloaded to
        """
        return self.content.request().download(local_path)

    @asyncio.coroutine
    def download_async(self, local_path):
        """Downloads the specified entity in async.

        Args:
            local_path (str): The path where the entity should be
                downloaded to
        """
        entity = yield from self.content.request().download_async(local_path)
        return entity

    @property
    def permissions(self):
        """The permissions for the ItemRequestBuilder

        Returns: 
            :class:`PermissionsCollectionRequestBuilder<onedrivesdk.request.permissions_collection.PermissionsCollectionRequestBuilder>`:
                A request builder created from the ItemRequestBuilder
        """
        return PermissionsCollectionRequestBuilder(self.append_to_request_url("permissions"), self._client)

    @property
    def subscriptions(self):
        """The subscriptions for the ItemRequestBuilder

        Returns: 
            :class:`SubscriptionsCollectionRequestBuilder<onedrivesdk.request.subscriptions_collection.SubscriptionsCollectionRequestBuilder>`:
                A request builder created from the ItemRequestBuilder
        """
        return SubscriptionsCollectionRequestBuilder(self.append_to_request_url("subscriptions"), self._client)

    @property
    def versions(self):
        """The versions for the ItemRequestBuilder

        Returns: 
            :class:`VersionsCollectionRequestBuilder<onedrivesdk.request.versions_collection.VersionsCollectionRequestBuilder>`:
                A request builder created from the ItemRequestBuilder
        """
        return VersionsCollectionRequestBuilder(self.append_to_request_url("versions"), self._client)

    @property
    def children(self):
        """The children for the ItemRequestBuilder

        Returns: 
            :class:`ChildrenCollectionRequestBuilder<onedrivesdk.request.children_collection.ChildrenCollectionRequestBuilder>`:
                A request builder created from the ItemRequestBuilder
        """
        return ChildrenCollectionRequestBuilder(self.append_to_request_url("children"), self._client)

    @property
    def tags(self):
        """The tags for the ItemRequestBuilder

        Returns: 
            :class:`TagsCollectionRequestBuilder<onedrivesdk.request.tags_collection.TagsCollectionRequestBuilder>`:
                A request builder created from the ItemRequestBuilder
        """
        return TagsCollectionRequestBuilder(self.append_to_request_url("tags"), self._client)

    @property
    def thumbnails(self):
        """The thumbnails for the ItemRequestBuilder

        Returns: 
            :class:`ThumbnailsCollectionRequestBuilder<onedrivesdk.request.thumbnails_collection.ThumbnailsCollectionRequestBuilder>`:
                A request builder created from the ItemRequestBuilder
        """
        return ThumbnailsCollectionRequestBuilder(self.append_to_request_url("thumbnails"), self._client)

    @property
    def content(self):
        """The content for the ItemRequestBuilder

        Returns: 
            :class:`ItemContentRequestBuilder<onedrivesdk.request.item_content.ItemContentRequestBuilder>`:
                A request builder created from the ItemRequestBuilder
        """
        return ItemContentRequestBuilder(self.append_to_request_url("content"), self._client)
    def create_session(self, item=None):
        """Executes the createSession method

        Args:
            item (:class:`ChunkedUploadSessionDescriptor<onedrivesdk.model.chunked_upload_session_descriptor.ChunkedUploadSessionDescriptor>`):
                Defaults to None, The item to use in the method request

        Returns:
            :class:`ItemCreateSessionRequestBuilder<onedrivesdk.request.item_create_session.ItemCreateSessionRequestBuilder>`:
                A ItemCreateSessionRequestBuilder for the method
        """
        return ItemCreateSessionRequestBuilder(self.append_to_request_url("upload.createSession"), self._client, item=item)

    def copy(self, name=None, parent_reference=None):
        """Executes the copy method

        Args:
            name (str):
                The name to use in the method request          
            parent_reference (:class:`ItemReference<onedrivesdk.model.item_reference.ItemReference>`):
                Defaults to None, The parent_reference to use in the method request

        Returns:
            :class:`ItemCopyRequestBuilder<onedrivesdk.request.item_copy.ItemCopyRequestBuilder>`:
                A ItemCopyRequestBuilder for the method
        """
        return ItemCopyRequestBuilder(self.append_to_request_url("action.copy"), self._client, name=name, parent_reference=parent_reference)

    def create_link(self, type):
        """Executes the createLink method

        Args:
            type (str):
                The type to use in the method request          

        Returns:
            :class:`ItemCreateLinkRequestBuilder<onedrivesdk.request.item_create_link.ItemCreateLinkRequestBuilder>`:
                A ItemCreateLinkRequestBuilder for the method
        """
        return ItemCreateLinkRequestBuilder(self.append_to_request_url("action.createLink"), self._client, type)

    def invite(self, recipients, require_sign_in=None, roles=None, send_invitation=None, message=None):
        """Executes the invite method

        Args:
            require_sign_in (bool):
                The require_sign_in to use in the method request          
            roles (str):
                The roles to use in the method request          
            recipients (:class:`Recipients<onedrivesdk.model.recipients.Recipients>`):
                The recipients to use in the method request
            send_invitation (bool):
                The send_invitation to use in the method request          
            message (str):
                The message to use in the method request          

        Returns:
            :class:`ItemInviteRequestBuilder<onedrivesdk.request.item_invite.ItemInviteRequestBuilder>`:
                A ItemInviteRequestBuilder for the method
        """
        return ItemInviteRequestBuilder(self.append_to_request_url("action.invite"), self._client, recipients, require_sign_in=require_sign_in, roles=roles, send_invitation=send_invitation, message=message)

    def delta(self, token=None):
        """Executes the delta method

        Args:
            token (str):
                The token to use in the method request          

        Returns:
            :class:`ItemDeltaRequestBuilder<onedrivesdk.request.item_delta.ItemDeltaRequestBuilder>`:
                A ItemDeltaRequestBuilder for the method
        """
        return ItemDeltaRequestBuilder(self.append_to_request_url("view.delta"), self._client, token=token)

    def search(self, q=None):
        """Executes the search method

        Args:
            q (str):
                The q to use in the method request          

        Returns:
            :class:`ItemSearchRequestBuilder<onedrivesdk.request.item_search.ItemSearchRequestBuilder>`:
                A ItemSearchRequestBuilder for the method
        """
        return ItemSearchRequestBuilder(self.append_to_request_url("view.search"), self._client, q=q)

from ..request.permissions_collection import PermissionsCollectionRequestBuilder
from ..request.subscriptions_collection import SubscriptionsCollectionRequestBuilder
from ..request.versions_collection import VersionsCollectionRequestBuilder
from ..request.children_collection import ChildrenCollectionRequestBuilder
from ..request.tags_collection import TagsCollectionRequestBuilder
from ..request.thumbnails_collection import ThumbnailsCollectionRequestBuilder
