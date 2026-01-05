import yaml
import pytest
import requests
import os
from core.client import APIClient

# -------------------------------
# 🔍 Pre-flight Health Check
# -------------------------------

BASE_URL = os.getenv("BASE_URL", "http://localhost:3001")

def pytest_sessionstart(session):
    """
    Pre-flight check: Ensure HR backend is UP before running tests
    """
    health_url = f"{BASE_URL}/api/health"

    try:
        response = requests.get(health_url, timeout=5)
        if response.status_code != 200:
            pytest.exit(
                f"\n❌ Backend health check failed: {health_url} "
                f"(status={response.status_code})",
                returncode=1
            )
    except requests.exceptions.RequestException as e:
        pytest.exit(
            f"\n❌ Backend is NOT reachable at {health_url}\nError: {e}",
            returncode=1
        )

# -------------------------------
# 🧪 Existing Fixtures (UNCHANGED)
# -------------------------------

@pytest.fixture(scope="session")
def env():
    with open("config/env.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def auth_token(env):
    return env["auth"]["token"]

@pytest.fixture
def api_client(env, auth_token):
    return APIClient(
        env["base_urls"]["api"],
        token=auth_token
    )

@pytest.fixture
def payroll_client(env, auth_token):
    return APIClient(
        env["base_urls"]["payroll"],
        token=auth_token
    )

@pytest.fixture
def rag_client(env):
    return APIClient(env["base_urls"]["rag"])
