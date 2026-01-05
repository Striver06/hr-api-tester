import pytest

def test_run_payroll(payroll_client):
    res = payroll_client.request("POST", "/api/payroll/run", json={})

    if res.status_code == 404:
        pytest.fail(
            "❌ Endpoint Missing (404): Payroll run API is not available "
            "or not enabled in this environment"
        )

    assert res.status_code == 200
