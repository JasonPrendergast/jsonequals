# jsonequals
json equality check inspired by [deepequals](https://github.com/epoberezkin/fast-deep-equal) compares the value of one json name/value pair to another name/value pair.  
# install

[installaion](https://www.osc.edu/resources/getting_started/howto/howto_install_your_own_python_modules)


# usage         
    
    testjson = json.loads(
        '{"description": "equal date objects",
         "value1": "2017-06-16T21:36:48.362Z",
         "value2": "2017-06-16T21:36:48.362Z",
         "equal": "True"}')
    tester(testjson)

# License
[MIT](https://github.com/JasonPrendergast/jsonequals/blob/master/LICENSE)
