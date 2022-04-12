import json
import unittest
import datetime


class Test_serializer(unittest.TestCase):
    def setUp(self):
        self.json_obj = serialize()

    def test_obj_type(self):
        self.assertEqual( type(self.json_obj) , type(json.dumps({})) )

    def test_atributes_type(self):
        obj = json.loads(self.json_obj)
        self.assertEqual( type(obj["required"][0]) , str )
        self.assertEqual( type(obj["required"][2]) , str )
        self.assertEqual( type(obj["required"][3]) , int )
        self.assertEqual( type(obj["required"][4]) , str ) 
    
    def test_date_format():
        obj = json.loads(self.json_obj)
        date = obj["required"][1]
        valid = True
        
        try:
            datetime.datetime.strptime(date, "%m/%d/%Y %H:%M")
        except:
            valid = False
        
        self.assertTrue(valid)

if __name__ == "__main__":
    unittest.main()
