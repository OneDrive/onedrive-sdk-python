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
'''

from .model.item_reference import ItemReference
from .model.upload_session import UploadSession
from .model.chunked_upload_session_descriptor import ChunkedUploadSessionDescriptor
from .model.audio import Audio
from .model.async_operation_status import AsyncOperationStatus
from .model.deleted import Deleted
from .model.file import File
from .model.file_system_info import FileSystemInfo
from .model.folder import Folder
from .model.hashes import Hashes
from .model.image import Image
from .model.location import Location
from .model.open_with_set import OpenWithSet
from .model.photo import Photo
from .model.quota import Quota
from .model.search_result import SearchResult
from .model.sharing_invitation import SharingInvitation
from .model.shared import Shared
from .model.sharing_link import SharingLink
from .model.special_folder import SpecialFolder
from .model.video import Video
from .model.identity_set import IdentitySet
from .model.identity import Identity
from .model.open_with_app import OpenWithApp
from .model.thumbnail import Thumbnail
from .model.drive import Drive
from .model.share import Share
from .model.item import Item
from .model.permission import Permission
from .model.thumbnail_set import ThumbnailSet
from .request.drive_request import DriveRequest
from .request.drive_request_builder import DriveRequestBuilder
from .request.share_request import ShareRequest
from .request.share_request_builder import ShareRequestBuilder
from .request.item_request import ItemRequest
from .request.item_request_builder import ItemRequestBuilder
from .request.permission_request import PermissionRequest
from .request.permission_request_builder import PermissionRequestBuilder
from .request.thumbnail_set_request import ThumbnailSetRequest
from .request.thumbnail_set_request_builder import ThumbnailSetRequestBuilder
from .request.thumbnail_request import ThumbnailRequest
from .request.thumbnail_request_builder import ThumbnailRequestBuilder
from .request.items_collection import ItemsCollectionRequest, ItemsCollectionRequestBuilder, ItemsCollectionPage, ItemsCollectionResponse
from .request.shared_collection import SharedCollectionRequest, SharedCollectionRequestBuilder, SharedCollectionPage, SharedCollectionResponse
from .request.special_collection import SpecialCollectionRequest, SpecialCollectionRequestBuilder, SpecialCollectionPage, SpecialCollectionResponse
from .request.items_collection import ItemsCollectionRequest, ItemsCollectionRequestBuilder, ItemsCollectionPage, ItemsCollectionResponse
from .request.permissions_collection import PermissionsCollectionRequest, PermissionsCollectionRequestBuilder, PermissionsCollectionPage, PermissionsCollectionResponse
from .request.versions_collection import VersionsCollectionRequest, VersionsCollectionRequestBuilder, VersionsCollectionPage, VersionsCollectionResponse
from .request.children_collection import ChildrenCollectionRequest, ChildrenCollectionRequestBuilder, ChildrenCollectionPage, ChildrenCollectionResponse
from .request.thumbnails_collection import ThumbnailsCollectionRequest, ThumbnailsCollectionRequestBuilder, ThumbnailsCollectionPage, ThumbnailsCollectionResponse
from .request.drives_collection import DrivesCollectionRequest, DrivesCollectionRequestBuilder, DrivesCollectionPage, DrivesCollectionResponse
from .request.shares_collection import SharesCollectionRequest, SharesCollectionRequestBuilder, SharesCollectionPage, SharesCollectionResponse
from .request.item_create_session import ItemCreateSessionRequest
from .request.item_copy import ItemCopyRequest
from .request.item_create_link import ItemCreateLinkRequest
from .request.item_delta import ItemDeltaRequest
from .request.item_search import ItemSearchRequest
from .request.item_delta_collection import ItemDeltaCollectionPage, ItemDeltaCollectionResponse
from .request.item_content_request import ItemContentRequest, ItemContentRequestBuilder
from .request.thumbnail_content_request import ThumbnailContentRequest, ThumbnailContentRequestBuilder
from .request.one_drive_client import OneDriveClient
from .auth_provider import AuthProvider
from .http_provider import HttpProvider
from .extensions.onedrivesdk_helper import *
from .extensions import *
import sys
if sys.version_info >= (3, 4, 0):
    from .version_bridge import *
