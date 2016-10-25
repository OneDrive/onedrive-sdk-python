import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import onedrivesdk
from onedrivesdk.http_response import HttpResponse
from onedrivesdk.request.children_collection import ChildrenCollectionRequest
from onedrivesdk.model.children_collection_page import ChildrenCollectionPage
from onedrivesdk.model.folder import Folder
import json


class TestCollections(unittest.TestCase):

    @patch('onedrivesdk.HttpProvider')
    @patch('onedrivesdk.AuthProvider')
    def test_page_creation(self, MockHttpProvider, MockAuthProvider):
        """
        Test page creation when there is no nextLink attached to the collection
        """
        response = HttpResponse(200, None, json.dumps({"value":[{"name":"test1", "folder":{}}, {"name":"test2"}]}))

        instance = MockHttpProvider.return_value
        instance.send.return_value = response

        instance = MockAuthProvider.return_value
        instance.authenticate.return_value = "blah"
        instance.authenticate_request.return_value = None

        http_provider = onedrivesdk.HttpProvider()
        auth_provider = onedrivesdk.AuthProvider()
        client = onedrivesdk.OneDriveClient("onedriveurl/", http_provider, auth_provider)

        items = client.drives["me"].items["root"].children.request().get()
        
        assert len(items) == 2
        assert isinstance(items, ChildrenCollectionPage)
        assert items[0].name == "test1"
        assert isinstance(items[0].folder, Folder)
        assert items[1].folder is None

    @patch('onedrivesdk.HttpProvider')
    @patch('onedrivesdk.AuthProvider')
    def test_paging(self, MockHttpProvider, MockAuthProvider):
        """
        Test paging of a file in situations where more than one page is available
        """
        response = HttpResponse(200, None, json.dumps({"@odata.nextLink":"testing", "value":[{"name":"test1", "folder":{}}, {"name":"test2"}]}))

        instance = MockHttpProvider.return_value
        instance.send.return_value = response

        instance = MockAuthProvider.return_value
        instance.authenticate.return_value = "blah"
        instance.authenticate_request.return_value = None

        http_provider = onedrivesdk.HttpProvider()
        auth_provider = onedrivesdk.AuthProvider()
        client = onedrivesdk.OneDriveClient("onedriveurl/", http_provider, auth_provider)

        items = client.drives["me"].items["root"].children.request().get()
        
        assert items._next_page_link is not None

        request = onedrivesdk.ChildrenCollectionRequest.get_next_page_request(items, client)
        assert isinstance(request, ChildrenCollectionRequest)
        assert isinstance(request.get(), ChildrenCollectionPage)

if __name__ == '__main__':
    unittest.main()
