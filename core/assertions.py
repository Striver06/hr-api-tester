def assert_status(response, expected):
    assert response.status_code == expected, (
        f"Expected {expected}, got {response.status_code}. "
        f"Response: {response.text}"
    )

def assert_json_has_keys(response, keys):
    body = response.json()
    for key in keys:
        assert key in body, f"Missing key '{key}' in response"
