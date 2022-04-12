import json
import unittest
import datetime
from json_serializer import serialize

TEST_CASES = (
    ['19', '11/30/15 13:05',   '3'	,'A'],
    ['4',  '11/30/15 13:06',   '3'	,'A'],
    ['33', '11/30/15 13:07',   '7'	,'A'],
    ['9',  '11/30/15 13:08',   '5'	,'C'],
    ['2',  '11/30/15 13:08',   '7'	,'C'],
    ['92', '11/30/15 13:09',   '3'	,'B']

    )

class Test_serializer(unittest.TestCase):
    def setUp(self):
        self.json_obj = serialize(test_case)

    def test_obj_type(self):
        self.assertEqual( type(self.json_obj) , type(json.dumps({})) )

    def test_atributes_type(self):
        obj = json.loads(self.json_obj)
        self.assertEqual( type(obj["required"][0]) , str )
        self.assertEqual( type(obj["required"][1]) , str )
        self.assertEqual( type(obj["required"][2]) , int )
        self.assertEqual( type(obj["required"][3]) , str ) 
    
    def test_date_format(self):
        obj = json.loads(self.json_obj)
        date = obj["required"][1]
        valid = True
        
        try:
            datetime.datetime.strptime(date, "%m/%d/%y %H:%M")
        except:
            valid = False
        
        self.assertTrue(valid)

if __name__ == "__main__":
    for test_case in TEST_CASES:
        unittest.main()
