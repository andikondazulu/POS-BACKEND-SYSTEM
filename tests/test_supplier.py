def test_list_suppliers_empty(client):
    response = client.get("/supplier/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_supplier_success(client):
    supplier_data = {
        "company_name": "Test Supplier",
        "contact_name": "John Doe",
        "email": "supplier@example.com",
        "supplier_phone": "1234567890",
        "address": "123 Test Street"
    }
    response = client.post("/supplier/", json=supplier_data)
    assert response.status_code == 201
    data = response.json()
    assert data["company_name"] == "Test Supplier"
    assert data["contact_name"] == "John Doe"
    assert data["email"] == "supplier@example.com"
    assert "supplier_id" in data
    assert data["is_active"] == True


def test_create_supplier_missing_company_name(client):
    response = client.post("/supplier/", json={
        "contact_name": "John Doe",
        "email": "test@example.com",
        "supplier_phone": "1234567890"
    })
    assert response.status_code == 422


def test_get_supplier_success(client):
    supplier_data = {
        "company_name": "Get Supplier",
        "contact_name": "Jane Doe",
        "email": "get@example.com",
        "supplier_phone": "0987654321"
    }
    create_response = client.post("/supplier/", json=supplier_data)
    supplier_id = create_response.json()["supplier_id"]
    
    response = client.get(f"/supplier/{supplier_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["company_name"] == "Get Supplier"
    assert data["supplier_id"] == supplier_id


def test_get_supplier_not_found(client):
    response = client.get("/supplier/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_update_supplier_success(client):
    supplier_data = {
        "company_name": "Original Supplier",
        "contact_name": "John Smith",
        "email": "original@example.com",
        "supplier_phone": "1111111111"
    }
    create_response = client.post("/supplier/", json=supplier_data)
    supplier_id = create_response.json()["supplier_id"]
    
    update_data = {
        "company_name": "Updated Supplier",
        "contact_name": "Jane Smith"
    }
    response = client.put(f"/supplier/{supplier_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["company_name"] == "Updated Supplier"
    assert data["contact_name"] == "Jane Smith"


def test_update_supplier_not_found(client):
    update_data = {
        "company_name": "Nonexistent"
    }
    response = client.put("/supplier/00000000-0000-0000-0000-000000000000", json=update_data)
    assert response.status_code == 404


def test_delete_supplier_success(client):
    supplier_data = {
        "company_name": "To Delete",
        "contact_name": "Delete Me",
        "email": "delete@example.com",
        "supplier_phone": "2222222222"
    }
    create_response = client.post("/supplier/", json=supplier_data)
    supplier_id = create_response.json()["supplier_id"]
    
    response = client.delete(f"/supplier/{supplier_id}")
    assert response.status_code == 204
    
    get_response = client.get(f"/supplier/{supplier_id}")
    assert get_response.status_code == 404


def test_delete_supplier_not_found(client):
    response = client.delete("/supplier/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_list_suppliers_with_data(client):
    client.post("/supplier/", json={
        "company_name": "Supplier 1",
        "contact_name": "Contact 1",
        "email": "s1@example.com",
        "supplier_phone": "1111111111"
    })
    client.post("/supplier/", json={
        "company_name": "Supplier 2",
        "contact_name": "Contact 2",
        "email": "s2@example.com",
        "supplier_phone": "2222222222"
    })
    
    response = client.get("/supplier/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2