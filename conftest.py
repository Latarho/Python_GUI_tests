import pytest
from fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application('D:\\Addressbook\\AddressBook.exe')
    request.addfinalizer(fixture.destroy)
    return fixture
