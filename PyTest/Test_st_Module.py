#module level - runs once per module(file)
#use module level setup and teardown when you want to execute the setup and teardown once in the current file
#eg open the db connection execute all testcases and atlast close the db connection
#setup_module --> only one per file
#setup_class() --> one per class
#setup_method() --> one per method
#setup_function() --> one per function

import pytest

def setup_module(module):
    print("Opening the DB connection")


def teardown_module(module):
    print("Closing the DB connection")


#testcase1
def test_read():
    print("Reading the DB")

#testcase 2
def test_write():
    print("Writing the data to the DB")

#testcase 3
def test_updating():
    print("Updating the DB")