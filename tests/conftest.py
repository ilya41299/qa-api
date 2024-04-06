import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://otus.ru",
        help="Request url",
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="Correct status code",
    )


@pytest.fixture(scope="session")
def request_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def correct_status_code(request):
    return int(request.config.getoption("--status_code"))
