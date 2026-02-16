#grouping - set of testcases run together - issue fix in the module

import pytest
#testcase 1
def testcase1():
    print("Testcase 1 is executed")

#testcase 2
@pytest.mark.sanity
def testcase2():
    print("Testcase 2 is executed")

#testcase 3
@pytest.mark.grr  #--> grouping
@pytest.mark.regression
def test_case3():
    print("Testcase 3 is executed")

