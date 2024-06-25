import pytest


@pytest.fixture(scope="session")
def browser():
    print("BROWSER!")
    yield
    print("close browser")