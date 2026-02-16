import sys,pytest

@pytest.mark.skipif(sys.platform!="linux",reason="This tests feature exclusive to Linux")
def test_linux_feature():
    print("Tested linux exclusive feature")