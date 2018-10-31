import sys
import pytest

from faker import Faker

sys.path.append('../..')
from word_count import WordCount

@pytest.fixture
def params():
    faker = Faker()
    return {'url': 'https://www.pontotel.com.br/', 
            'word': faker.word()}

def test_islist(params):
    word_count = WordCount(**params)
    response = word_count.count_words()
    assert isinstance(response, list)

def test_keyword(params):
    word_count = WordCount(**params)
    response = word_count.count_words()
    assert params['word'] in response[0]['word']

def test_url(params):
    word_count = WordCount(**params)
    response = word_count.count_words()
    assert params['url'] in response[0]['url']

def test_value(params):
    word_count = WordCount(**params)
    response = word_count.count_words()
    assert isinstance(response[0]['value'], int)
