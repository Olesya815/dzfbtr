import requests
import re


def test_get_uuid():
    response = requests.get('http://www.httpbin.org/uuid')
    uuid = response.text[13:-4]
    sample = re.compile(('[0-9a-z]{8}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{12}'))

    assert sample.match(uuid).string == uuid
    assert response.status_code == 200





