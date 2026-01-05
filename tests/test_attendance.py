def test_attendance_list(api_client):
    res = api_client.request("GET", "/api/attendance/punch/status")
    assert res.status_code == 200
