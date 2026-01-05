import requests

class APIClient:
    def __init__(self, base_url, token=None, timeout=10):
        self.base_url = base_url
        self.token = token
        self.timeout = timeout

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def request(self, method, path, **kwargs):
        """
        kwargs can include: json, params, data, headers, etc.
        Behaves like requests.request()
        """
        return requests.request(
            method=method,
            url=f"{self.base_url}{path}",
            headers=self._headers(),
            timeout=self.timeout,
            **kwargs
        )
