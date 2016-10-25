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


    def test_serialization_different_datetime(self):
        """
        Test the serialization of the dict-backed models, seeing that
        the correct objects are returned when called. Specifically,
        ensure that the datetime can be parsed correctly when the format
        does not fit exactly what we always return
        """
        ref = ItemReference();
        ref._prop_dict = {"id": "thisisa!test"}

        response = {"name":"test1", "folder":{}, "parentReference":ref._prop_dict, "lastModifiedDateTime": "2015-07-09T22:22:53.99Z"}

        item = Item();
        item._prop_dict = response

        assert type(item.folder) is Folder
        assert item.name == "test1"
        assert type(item.parent_reference) is ItemReference
        assert item.parent_reference.id == "thisisa!test"
        assert type(item.last_modified_date_time) == datetime
        assert item.last_modified_date_time.isoformat()+"Z" == "2015-07-09T22:22:53.990000Z"

        timenow = datetime.now()
        item.last_modified_date_time = timenow
        assert item.last_modified_date_time.isoformat() == timenow.isoformat()

        timenow = timenow.replace(microsecond=235)
        item.last_modified_date_time = timenow
        assert item.last_modified_date_time.isoformat() == timenow.isoformat()

if __name__ == '__main__':
    unittest.main()
