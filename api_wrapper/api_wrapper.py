import requests

class APIWrapper:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.example.com"

    def get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()
