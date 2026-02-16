import requests


base_url="http://127.0.0.1:5000/customers"
customer_id=None

#POST-Create customer
def test_create_customer():
    global customer_id

    payload={
        "Name": "Rion",
        "E-mail": "rion@test.com",
        "Balance": 5000
    }
    response=requests.post(base_url,json=payload)
    assert response.status_code==201

    data=response.json()
    assert "ID" in data
    assert data["Name"]==payload["Name"]

    customer_id=data["ID"]

#GET- Retrieve Customer
def test_get_customer():
    response=requests.get(f"{base_url}/{customer_id}")

    assert response.status_code==200
    data=response.json()
    assert data["E-mail"]=="rion@test.com"
    assert data["Balance"]==5000

#PUT - Update customer
def test_update_customer():
    payload={
        "E-mail": "updated@test.com"
    }
    response=requests.put(f"{base_url}/{customer_id}",json=payload)
    assert response.status_code==200

    data=response.json()
    assert data["E-mail"]=="updated@test.com"

#DELETE - Remove Customer
def test_delete_customer():
    response=requests.delete(f"{base_url}/{customer_id}")
    assert response.status_code==204

    response=requests.get(f"{base_url}/{customer_id}")
    assert response.status_code==404