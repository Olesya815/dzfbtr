import pytest as pytest
import requests


def status_codes(codes):
    response = requests.get(f'http://www.httpbin.org/status/{codes}')
    return response.status_code


@pytest.mark.parametrize("codes, expected", [(100, 100)])
def test_status_one_hundred(codes, expected):
    assert status_codes(codes) == expected


@pytest.mark.parametrize("codes, expected", [(200, 200)])
def test_status_one_hundred(codes, expected):
    assert status_codes(codes) == expected


@pytest.mark.parametrize("codes, expected", [(300, 300)])
def test_status_three_hundred(codes, expected):
    assert status_codes(codes) == expected


@pytest.mark.parametrize("codes, expected", [(400, 400)])
def test_status_four_hundred(codes, expected):
    assert status_codes(codes) == expected


@pytest.mark.parametrize("codes, expected", [(500, 500)])
def test_status_five_hundred(codes, expected):
    assert status_codes(codes) == expected






# def status_messages():
#     mess = status_codes()
#     response = requests.get(f'http://www.httpbin.org/status/{mess}')
#     print(response.text)
#     return response.reason

# @pytest.mark.parametrize("message, expected", [('Success', "Success")])
# def test_status_oe_hundred(message, expected):
#     assert status_messages() == expected