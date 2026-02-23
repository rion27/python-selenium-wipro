#skip - if there are defects
#skip - if the test cases are absolute
#windows , mobile - os dependency
#browsers - Firefox, IE, Chrome, Safari

import pytest
#testcase 1
def testcase1():
    print("Testcase 1 is executed")

#testcase 2
@pytest.mark.skip #--> can add reason too like .skip(reason="feature not available")
def testcase2():
    print("Testcase 2 is executed")

#testcase 3
def test_case3():
    print("Testcase 3 is executed")

#testcase 4  does not run as it is in wrong naming convention
def openbrowser():
    print("Opening the browser")