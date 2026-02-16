#parameterization testing multiple set of test data with the same function
#no parameters used
#@pytest.mark.parameterize()

#no parameters used
def test_add1():
    assert 2+3==5

def test_add2():
    assert 4+5==9
import pytest
@pytest.mark.parametrize("a,b,result",[
        (2,3,5),
        (4,5,9),
        (10,2,12)
])


def test_add(a,b,result):
    assert a+b==result

#single parameter
@pytest.mark.parametrize("number",[1,2,3,4,5])
def test_even(number):
    assert number%2==0
#dictonary items
@pytest.mark.parametrize("payload",[{"name": "john","age":25},{"name": "alice","age":17}])
def test_create_user(payload):
    assert payload["age"]>18