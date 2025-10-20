
import requests

class StripeAPI:
    def __init__(self, base_url=None, headers=None):
        self.base_url = base_url.rstrip("/") if base_url else ""
        self.headers = headers or {}

    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=headers or self.headers)

    def post(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        print(payload)
        return requests.post(url,params=payload ,json=payload, headers=headers or self.headers)

    def put(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.put(url, json=payload, headers=headers or self.headers)

    def delete(self, endpoint, headers=None, payload=None):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url, headers=headers or self.headers, json=payload)
