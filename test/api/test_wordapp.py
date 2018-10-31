import json
import pytest
import sys

from faker import Faker

sys.path.append('../..')
from api.wordapp import app


@pytest.fixture
def application():
    application = app.test_client()
    application.testing = True
    return application

@pytest.fixture
def params():
    faker = Faker()
    return {'url': 'https://www.pontotel.com.br/', 
            'word': faker.word()}

def test_get(application, params):
    response = application.get('/', query_string=params)
    assert response.status_code == 200
    
