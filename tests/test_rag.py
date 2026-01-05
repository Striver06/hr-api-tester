import pytest
import requests

def test_rag_query(rag_client):
    try:
        res = rag_client.request(
            "POST",
            "/query",
            json={"question": "What is leave policy?"}
        )
    except requests.exceptions.ConnectionError:
        pytest.skip("⚠️ Dependency Down: RAG server is not reachable")

    if res.status_code in (502, 503):
        pytest.skip("⚠️ Dependency Down: RAG service is unavailable")

    assert res.status_code == 200
    assert "answer" in res.json()
