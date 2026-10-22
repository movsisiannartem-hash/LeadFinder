
from unittest.mock import Mock, patch

from utils.website_checker import check_website


def test_check_website_none():
    assert check_website(None) is False


@patch("utils.website_checker.requests.get")
def test_check_website_success(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    assert check_website("https://example.com") is True


@patch("utils.website_checker.requests.get")
def test_check_website_request_error(mock_get):
    import requests

    mock_get.side_effect = requests.exceptions.Timeout

    assert check_website("https://example.com") is False
