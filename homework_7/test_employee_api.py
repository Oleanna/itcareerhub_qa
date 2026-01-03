
def test_create_employee(employee_api):
    payload = {
          "first_name": "Alex",
          "last_name": "Alex",
          "middle_name": "Alex",
          "company_id": 3,
          "email": "Alex@example.com",
          "phone": "000000",
          "birthdate": "2026-01-03",
          "is_active": True
        }

    response = employee_api.create_employee(payload)

    assert response.status_code == 200
    assert response.json()["first_name"] == "Alex"

def test_get_employee(employee_api):

    response = employee_api.get_employee(10)

    assert response.status_code == 200

    assert response.json()["first_name"] == "Alex"

def test_update_employee(employee_api):
    payload = {
          "last_name": "Alex",
          "email": "Alex@example.com",
          "phone": "55555",
          "is_active": True
        }

    response = employee_api.update_employee(12, payload)

    assert response.status_code == 200
    assert response.json()["last_name"] == "Alex"

