import pytest
from homework_7.employee_api import EmployeeApi


@pytest.fixture
def employee_api():
    return EmployeeApi(
        base_url="http://5.101.50.27:8000",
        client_token=""
    )
