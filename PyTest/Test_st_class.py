#used inside the classes
#it will run for every class definition

import pytest

class Testclass1:
    #class level set up
    def setup_class(cls):
        print("API Authorization needed with username and password")

    def teardown_class(cls):
        print("API Authorization closed")

    # setup at method level
    def setup_method(method):
        print("opening the browser")

    # teardown at method level
    def teardown_method(method):
        print("closing the browser")

    def testcase1(self):
        print("Testcase 1 is executed")

    # testcase 2
    @pytest.mark.sanity
    def testcase2(self):
        print("Testcase 2 is executed")

    # testcase 3
    def test_case3(self):
        print("Testcase 3 is executed")
class Testclass2:

    # testcase 3
    def testcase1(self):
        print("Testcase 1 is executed")

    # testcase 2
    def testcase2(self):
        print("Testcase 2 is executed")

    # testcase 3
    def test_case3(self):
        print("Testcase 3 is executed")