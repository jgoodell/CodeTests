# Directions

The assessement is coded as a python package, the utillity can be
imported and run in the python shell with

``` python
>>> import hex_to_base64
>>> hex_to_base64.utils.translate('45766964696e74')
'RXZpZGludA==\n'
>>> 
```

or run the unit test to confirm the result

``` shell
hex-to-base64$ python setup.py test
/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/dist.py:285: UserWarning: Normalizing '0.1.0dev1' to '0.1.0.dev1'
  normalized_version,
running test
running egg_info
writing hextobase64.egg-info/PKG-INFO
writing top-level names to hextobase64.egg-info/top_level.txt
writing dependency_links to hextobase64.egg-info/dependency_links.txt
reading manifest file 'hextobase64.egg-info/SOURCES.txt'
writing manifest file 'hextobase64.egg-info/SOURCES.txt'
running build_ext
test_success (tests.test_utils.TestHexBase64) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```

The code is in hex_to_base64.utils.py, and the tests are in
tests/test_utils.py.