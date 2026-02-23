import pytest
@pytest.mark.xfail(reason="Bug #123")
def case_test():
    print("Executed")
    assert 5+6==20

#testcase 1
def testcase1():
    print("Testcase 1 is executed")

#testcase 2
def testcase2():
    print("Testcase 2 is executed")

#testcase 3

def test_case3():
    print("Testcase 3 is executed")