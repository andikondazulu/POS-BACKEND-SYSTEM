def test_list_sales_empty(client):
    response = client.get("/sale/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_sale_success(client):
    sale_data = {
        "customer_id": "00000000-0000-0000-0000-000000000000",
        "user_id": "00000000-0000-0000-0000-000000000000",
        "sale_date": "2024-01-01T00:00:00",
        "subtotal": 100.00,
        "tax_amount": 10.00,
        "total_amount": 110.00,
        "status": "completed"
    }
    response = client.post("/sale/", json=sale_data)
    assert response.status_code == 201
    data = response.json()
    assert data["subtotal"] == "100.00"
    assert data["tax_amount"] == "10.00"
    assert data["total_amount"] == "110.00"
    assert data["status"] == "completed"
    assert "sale_id" in data


def test_create_sale_missing_fields(client):
    response = client.post("/sale/", json={
        "subtotal": 100.00
    })
    assert response.status_code == 422


def test_get_sale_success(client):
    sale_data = {
        "customer_id": "00000000-0000-0000-0000-000000000000",
        "user_id": "00000000-0000-0000-0000-000000000000",
        "sale_date": "2024-01-01T00:00:00",
        "subtotal": 200.00,
        "tax_amount": 20.00,
        "total_amount": 220.00,
        "status": "completed"
    }
    create_response = client.post("/sale/", json=sale_data)
    sale_id = create_response.json()["sale_id"]
    
    response = client.get(f"/sale/{sale_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["sale_id"] == sale_id
    assert data["subtotal"] == "200.00"


def test_get_sale_not_found(client):
    response = client.get("/sale/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_update_sale_success(client):
    sale_data = {
        "customer_id": "00000000-0000-0000-0000-000000000000",
        "user_id": "00000000-0000-0000-0000-000000000000",
        "sale_date": "2024-01-01T00:00:00",
        "subtotal": 100.00,
        "tax_amount": 10.00,
        "total_amount": 110.00,
        "status": "completed"
    }
    create_response = client.post("/sale/", json=sale_data)
    sale_id = create_response.json()["sale_id"]
    
    update_data = {
        "subtotal": 150.00,
        "total_amount": 165.00,
        "status": "cancelled"
    }
    response = client.put(f"/sale/{sale_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["subtotal"] == "150.00"
    assert data["total_amount"] == "165.00"
    assert data["status"] == "cancelled"


def test_update_sale_not_found(client):
    update_data = {
        "subtotal": 150.00
    }
    response = client.put("/sale/00000000-0000-0000-0000-000000000000", json=update_data)
    assert response.status_code == 404


def test_delete_sale_success(client):
    sale_data = {
        "customer_id": "00000000-0000-0000-0000-000000000000",
        "user_id": "00000000-0000-0000-0000-000000000000",
        "sale_date": "2024-01-01T00:00:00",
        "subtotal": 100.00,
        "tax_amount": 10.00,
        "total_amount": 110.00,
        "status": "completed"
    }
    create_response = client.post("/sale/", json=sale_data)
    sale_id = create_response.json()["sale_id"]
    
    response = client.delete(f"/sale/{sale_id}")
    assert response.status_code == 204
    
    get_response = client.get(f"/sale/{sale_id}")
    assert get_response.status_code == 404


def test_delete_sale_not_found(client):
    response = client.delete("/sale/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_list_sales_with_data(client):
    client.post("/sale/", json={
        "customer_id": "00000000-0000-0000-0000-000000000000",
        "user_id": "00000000-0000-0000-0000-000000000000",
        "sale_date": "2024-01-01T00:00:00",
        "subtotal": 100.00,
        "tax_amount": 10.00,
        "total_amount": 110.00,
        "status": "completed"
    })
    client.post("/sale/", json={
        "customer_id": "00000000-0000-0000-0000-000000000000",
        "user_id": "00000000-0000-0000-0000-000000000000",
        "sale_date": "2024-01-01T00:00:00",
        "subtotal": 200.00,
        "tax_amount": 20.00,
        "total_amount": 220.00,
        "status": "completed"
    })
    
    response = client.get("/sale/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2