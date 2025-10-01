import re


def is_valid_email(email: str) -> bool:

    pattern = r'^[^@]+@[^@]+\.[^@]+$'
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    test_emails = [
        "beispiel@domain.de",
        "invalid-email",
        "test@.com",
    ]
    for email in test_emails:
        print(f"{email}: {is_valid_email(email)}")
