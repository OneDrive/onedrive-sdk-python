import unittest

from onedrivesdk.model.folder import Folder
from onedrivesdk.model.item import Item
from onedrivesdk.model.item_reference import ItemReference
from datetime import datetime


class TestModels(unittest.TestCase):

    name = "test1"
    id = "thisisa!test"

    def test_serialization(self):
        """
        Test the serialization of the dict-backed models, seeing that
        the correct objects are returned when called
        """
        ref = ItemReference();
        ref._prop_dict = {"id": self.id}

        response = {"name":self.name, "folder":{}, "parentReference":ref._prop_dict, "lastModifiedDateTime": "2015-07-09T22:22:53.993000Z"}

        item = Item();
        item._prop_dict = response

        assert isinstance(item.folder, Folder)
        assert item.name == self.name
        assert isinstance(item.parent_reference, ItemReference)
        assert item.parent_reference.id == self.id
        assert isinstance(item.last_modified_date_time, datetime)
        assert item.last_modified_date_time.isoformat()+"Z" == response["lastModifiedDateTime"]


    def test_serialization_different_datetime(self):
        """
        Test the serialization of the dict-backed models, seeing that
        the correct objects are returned when called. Specifically,
        ensure that the datetime can be parsed correctly when the format
        does not fit exactly what we always return
        """
        ref = ItemReference();
        ref._prop_dict = {"id": self.id}

        response = {"name":self.name, "folder":{}, "parentReference":ref._prop_dict, "lastModifiedDateTime": "2015-07-09T22:22:53.99Z"}

        item = Item();
        item._prop_dict = response

        assert isinstance(item.folder, Folder)
        assert item.name == self.name
        assert isinstance(item.parent_reference, ItemReference)
        assert item.parent_reference.id == self.id
        assert isinstance(item.last_modified_date_time, datetime)
        assert item.last_modified_date_time.isoformat()+"Z" == "2015-07-09T22:22:53.990000Z"

        response = {"name":self.name, "folder":{}, "parentReference":ref._prop_dict, "lastModifiedDateTime": "2015-07-09T22:22:53Z"}
        item._prop_dict = response

        assert isinstance(item.folder, Folder)
        assert item.name == self.name
        assert isinstance(item.parent_reference, ItemReference)
        assert item.parent_reference.id == self.id
        assert isinstance(item.last_modified_date_time, datetime)
        assert item.last_modified_date_time.isoformat()+"Z" == "2015-07-09T22:22:53Z"

        timenow = datetime.now()
        item.last_modified_date_time = timenow
        assert item.last_modified_date_time.isoformat() == timenow.isoformat()
        assert item._prop_dict['lastModifiedDateTime'] == timenow.isoformat()+"Z"

        timenow = timenow.replace(microsecond=235)
        item.last_modified_date_time = timenow
        assert item.last_modified_date_time.isoformat() == timenow.isoformat()
        assert item._prop_dict['lastModifiedDateTime'] == timenow.isoformat()+"Z"

        timenow = timenow.replace(microsecond=0)
        item.last_modified_date_time = timenow
        assert item.last_modified_date_time.isoformat() == timenow.isoformat()
        assert item._prop_dict['lastModifiedDateTime'] == timenow.isoformat()+".0Z"

if __name__ == '__main__':
    unittest.main()
