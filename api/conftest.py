import pytest
import requests
from utils.configs.url_links import get_base_api_url

@pytest.fixture
def api_client():

    base_url = get_base_api_url()

    session = requests.Session()
    session.base_url = base_url

    def _post(endpoint, **kwargs):
        session.post(session.base_url + endpoint, **kwargs)

    def _get(endpoint, **kwargs):
        session.get(session.base_url + endpoint, **kwargs)

    session.post = _post
    session.get = _get

    yield session
    session.close()
