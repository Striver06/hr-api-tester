from core.client import APIClient

def login(api_base_url, email, password):
    client = APIClient(api_base_url)

    res = client.request(
        "POST",
        "/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    assert res.status_code == 200, res.text
    return res.json()["token"]
