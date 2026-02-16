#function level setups and teardown
#these run before and after each test function
import pytest
#setup at function level
def setup_function(function):
    print("opening the browser")

#teardown at function level
def teardown_function(function):
    print("closing the browser")

#testcase1
def testcase1():
    print("Testcase 1 is executed")

#testcase 2
@pytest.mark.regression
def testcase2():
    print("Testcase 2 is executed")

#testcase 3
def test_case3():
    print("Testcase 3 is executed")

