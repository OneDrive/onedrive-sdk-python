import unittest

from onedrivesdk.model.folder import Folder
from onedrivesdk.model.item import Item
from onedrivesdk.model.item_reference import ItemReference
from datetime import datetime


class TestModels(unittest.TestCase):

    def test_serialization(self):
        """
        Test the serialization of the dict-backed models, seeing that
        the correct objects are returned when called
        """
        ref = ItemReference();
        ref._prop_dict = {"id": "thisisa!test"}

        response = {"name":"test1", "folder":{}, "parentReference":ref._prop_dict, "lastModifiedDateTime": "2015-07-09T22:22:53.993000Z"}

        item = Item();
        item._prop_dict = response

        assert type(item.folder) is Folder
        assert item.name == "test1"
        assert type(item.parent_reference) is ItemReference
        assert item.parent_reference.id == "thisisa!test"
        assert type(item.last_modified_date_time) == datetime
        assert item.last_modified_date_time.isoformat()+"Z" == response["lastModifiedDateTime"]


if __name__ == '__main__':
    unittest.main()
