import requests


class EmployeeApi:
    def __init__(self, base_url: str, client_token: str):
        self.base_url = base_url
        self.client_token = client_token

    def create_employee(self, payload: dict):
        return requests.post(
            f"{self.base_url}/employee/create",
            json=payload
        )

    def get_employee(self, employee_id: int):
        return requests.get(
            f"{self.base_url}/employee/info/{employee_id}"
        )

    def update_employee(self, employee_id: int, payload: dict):
        return requests.patch(
            f"{self.base_url}/employee/change/{employee_id}",
            params={"client_token": self.client_token},
            json=payload
        )
