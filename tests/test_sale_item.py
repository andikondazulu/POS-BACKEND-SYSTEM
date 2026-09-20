def test_list_sale_items_empty(client):
    response = client.get("/sale-item/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_sale_item_success(client):
    sale_item_data = {
        "sale_id": "00000000-0000-0000-0000-000000000000",
        "product_id": "00000000-0000-0000-0000-000000000000",
        "quantity": 2,
        "unit_price": 50.00,
        "total_price": 100.00
    }
    response = client.post("/sale-item/", json=sale_item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["quantity"] == 2
    assert data["unit_price"] == "50.00"
    assert data["total_price"] == "100.00"
    assert "sale_item_id" in data


def test_create_sale_item_missing_fields(client):
    response = client.post("/sale-item/", json={
        "quantity": 2
    })
    assert response.status_code == 422


def test_get_sale_item_success(client):
    sale_item_data = {
        "sale_id": "00000000-0000-0000-0000-000000000000",
        "product_id": "00000000-0000-0000-0000-000000000000",
        "quantity": 3,
        "unit_price": 25.00,
        "total_price": 75.00
    }
    create_response = client.post("/sale-item/", json=sale_item_data)
    sale_item_id = create_response.json()["sale_item_id"]
    
    response = client.get(f"/sale-item/{sale_item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["sale_item_id"] == sale_item_id
    assert data["quantity"] == 3


def test_get_sale_item_not_found(client):
    response = client.get("/sale-item/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_update_sale_item_success(client):
    sale_item_data = {
        "sale_id": "00000000-0000-0000-0000-000000000000",
        "product_id": "00000000-0000-0000-0000-000000000000",
        "quantity": 2,
        "unit_price": 50.00,
        "total_price": 100.00
    }
    create_response = client.post("/sale-item/", json=sale_item_data)
    sale_item_id = create_response.json()["sale_item_id"]
    
    update_data = {
        "quantity": 5,
        "unit_price": 60.00,
        "total_price": 300.00
    }
    response = client.put(f"/sale-item/{sale_item_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 5
    assert data["unit_price"] == "60.00"
    assert data["total_price"] == "300.00"


def test_update_sale_item_not_found(client):
    update_data = {
        "quantity": 5
    }
    response = client.put("/sale-item/00000000-0000-0000-0000-000000000000", json=update_data)
    assert response.status_code == 404


def test_delete_sale_item_success(client):
    sale_item_data = {
        "sale_id": "00000000-0000-0000-0000-000000000000",
        "product_id": "00000000-0000-0000-0000-000000000000",
        "quantity": 2,
        "unit_price": 50.00,
        "total_price": 100.00
    }
    create_response = client.post("/sale-item/", json=sale_item_data)
    sale_item_id = create_response.json()["sale_item_id"]
    
    response = client.delete(f"/sale-item/{sale_item_id}")
    assert response.status_code == 204
    
    get_response = client.get(f"/sale-item/{sale_item_id}")
    assert get_response.status_code == 404


def test_delete_sale_item_not_found(client):
    response = client.delete("/sale-item/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_list_sale_items_with_data(client):
    client.post("/sale-item/", json={
        "sale_id": "00000000-0000-0000-0000-000000000000",
        "product_id": "00000000-0000-0000-0000-000000000000",
        "quantity": 2,
        "unit_price": 50.00,
        "total_price": 100.00
    })
    client.post("/sale-item/", json={
        "sale_id": "00000000-0000-0000-0000-000000000000",
        "product_id": "00000000-0000-0000-0000-000000000000",
        "quantity": 3,
        "unit_price": 25.00,
        "total_price": 75.00
    })
    
    response = client.get("/sale-item/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2