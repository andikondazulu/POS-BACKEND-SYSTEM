def test_list_customers_empty(client):
    response = client.get("/customer/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_customer_success(client):
    customer_data = {
        "first_name": "John",
        "last_name": "Doe",
        "phone_no": "1234567890",
        "address": "123 Test Street"
    }
    response = client.post("/customer/", json=customer_data)
    assert response.status_code == 201
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["phone_no"] == "1234567890"
    assert "customer_id" in data
    assert data["is_active"] == True


def test_create_customer_missing_first_name(client):
    response = client.post("/customer/", json={
        "last_name": "Doe",
        "phone_no": "1234567890"
    })
    assert response.status_code == 422


def test_create_customer_missing_last_name(client):
    response = client.post("/customer/", json={
        "first_name": "John",
        "phone_no": "1234567890"
    })
    assert response.status_code == 422


def test_get_customer_success(client):
    customer_data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "phone_no": "0987654321"
    }
    create_response = client.post("/customer/", json=customer_data)
    customer_id = create_response.json()["customer_id"]
    
    response = client.get(f"/customer/{customer_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Jane"
    assert data["customer_id"] == customer_id


def test_get_customer_not_found(client):
    response = client.get("/customer/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_update_customer_success(client):
    customer_data = {
        "first_name": "Original",
        "last_name": "Customer"
    }
    create_response = client.post("/customer/", json=customer_data)
    customer_id = create_response.json()["customer_id"]
    
    update_data = {
        "first_name": "Updated",
        "last_name": "Customer"
    }
    response = client.put(f"/customer/{customer_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Updated"
    assert data["last_name"] == "Customer"


def test_update_customer_not_found(client):
    update_data = {
        "first_name": "Nonexistent"
    }
    response = client.put("/customer/00000000-0000-0000-0000-000000000000", json=update_data)
    assert response.status_code == 404


def test_delete_customer_success(client):
    customer_data = {
        "first_name": "To",
        "last_name": "Delete"
    }
    create_response = client.post("/customer/", json=customer_data)
    customer_id = create_response.json()["customer_id"]
    
    response = client.delete(f"/customer/{customer_id}")
    assert response.status_code == 204
    
    get_response = client.get(f"/customer/{customer_id}")
    assert get_response.status_code == 404


def test_delete_customer_not_found(client):
    response = client.delete("/customer/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_list_customers_with_data(client):
    client.post("/customer/", json={"first_name": "C1", "last_name": "Doe"})
    client.post("/customer/", json={"first_name": "C2", "last_name": "Smith"})
    
    response = client.get("/customer/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2