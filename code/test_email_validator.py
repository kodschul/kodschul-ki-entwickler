import pytest
from email_validator import is_valid_email


@pytest.mark.parametrize("email", [
    "a@b.co",
    "user.name+tag@sub.domain.com",
    "1234567890@numbers123.com",
])
def test_is_valid_email_positive_edge_cases(email):
    assert is_valid_email(email) is True


@pytest.mark.parametrize("email", [
    "@domain.com",
    "user@domain",
    "user@@domain.com",
])
def test_is_valid_email_negative_edge_cases(email):
    assert is_valid_email(email) is False
