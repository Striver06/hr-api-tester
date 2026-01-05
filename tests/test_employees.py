import pytest
from utils.data_factory import employee_payload

def test_create_employee(api_client):
    payload = employee_payload()
    res = api_client.request("POST", "/api/employees", json=payload)

    if res.status_code == 500:
        pytest.fail(
            "❌ Backend Error (500): Server crashed while creating employee"
        )

    assert res.status_code == 201
