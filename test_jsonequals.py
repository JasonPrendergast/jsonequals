import jsonequals
import json

class test_jsonequals:
    def __init__(self,testjson):
        self.testjson=testjson

    def test_equals(self):
        deepe = jsonequals.jsonequals(self.testjson)
        result = deepe.jsonequals()
        return result

def tester(testerjson):
    testjson = testerjson
    testy = test_jsonequals(testjson)
    testy = testy.test_equals()
    if str(testy) == testjson['equal']:
        print('pass test equal_date_objects')
    else:
        print('fail test equal_date_objects')

if __name__ == "__main__":
    testjson = json.loads(
        '{"description": "equal date objects", '
        '"value1": "2017-06-16T21:36:48.362Z", '
        '"value2": "2017-06-16T21:36:48.362Z",'
        '"equal": "True"}')
    tester(testjson)

    testjson = json.loads(
        '{"description": "not equal date objects", '
        '"value1": "2017-06-16T21:36:48.362Z", '
        '"value2": "2017-01-01T00:00:00.000Z",'
        '"equal": "False"}')
    tester(testjson)

    testjson = json.loads(
        '{"description": "date and string are not equal", '
        '"value1": "2017-06-16T21:36:48.362Z", '
        '"value2": "Foo",'
        '"equal": "False"}')
    tester(testjson)

    testjson = json.loads(
        '{"description": "date and null are not equal", '
        '"value1": "new Date(2017-06-16T21:36:48.362Z)", '
        '"value2": "",'
        '"equal": "False"}')
    tester(testjson)

    testjson = json.loads(
        '{"description": "equal string",'
        ' "value1": "/foo/", '
        '"value2": "/foo/",'
        '"equal": "True"}')
    tester(testjson)

    testjson = json.loads(
        '{"description": "not equal string (different pattern)", '
        '"value1": "/foo/", '
        '"value2": "/bar/",'
        '"equal": "False"}')
    tester(testjson)

    