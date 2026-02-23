#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)
import pytest

@pytest.mark.xfail(reason="Known bug in the third-party library")
def test_function_with_bug():
    assert (1+1) == 3 #this is always fail as expected

#testcase 1
@pytest.mark.sanity
def testcase1():
    print("Testcase 1 is executed")

#testcase 2
@pytest.mark.regression
def testcase2():
    print("Testcase 2 is executed")

#testcase 3
@pytest.mark.grr
def test_case3():
    print("Testcase 3 is executed")