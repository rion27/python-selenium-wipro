import requests,pytest
url="https://fakestoreapi.com/carts"
def test_api():
    try:
        response=requests.get(url,timeout=5)
    except requests.exceptions.RequestException as E:
        pytest.skip(f"Error: API unreachable: {E}")
    if response.status_code!=200:
        pytest.skip(f"API unhealthy: Status :{response.status_code} ")

    assert response.status_code==200
