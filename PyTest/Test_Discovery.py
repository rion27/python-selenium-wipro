# unit testing is type of testing done by the developers
# what component they have developed they do the testing for it before integrating it to the other modules
# get defects earlier
# Pytest in python , junit and nunit - java
# pytest is used by developers and testers

#test discovery - rules used to create the pytest tests
#files should start with "test"
#functions also should start with "test"

# -v verbose -shows detailed output
#-s show print request

import pytest
#testcase 1
def testcase1():
    print("Testcase 1 is executed")

#testcase 2
def testcase2():
    print("Testcase 2 is executed")

#testcase 3
def test_case3():
    print("Testcase 3 is executed")

#testcase 4
def openbrowser():
    print("Opening the browser")

#pytest .\Test_Discovery.py to run in cmd line
#pytest .\Test_Discovery.py -v -s --html=filename.html ---> to generate report