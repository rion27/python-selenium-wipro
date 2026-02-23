import pytest

def test_1():
    print("Gallery feature tested")

def test2():
    print("Posting feature tested")

@pytest.mark.skip(reason="AI feature not implemented yet")
def test3():
    print("AI feature tested ")