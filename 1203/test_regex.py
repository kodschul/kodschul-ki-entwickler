import unittest
from regex_checker import is_valid_email


class TestIsValidEmailValid(unittest.TestCase):
    """Gültige Adressen – alle müssen True zurückgeben."""

    def test_simple(self):
        self.assertTrue(is_valid_email("alice@example.com"))

    def test_subdomain(self):
        self.assertTrue(is_valid_email("alice@mail.example.com"))

    def test_plus_tag(self):
        self.assertTrue(is_valid_email("alice+filter@example.com"))

    def test_underscore(self):
        self.assertTrue(is_valid_email("user_name@example.com"))

    def test_hyphen_in_local(self):
        self.assertTrue(is_valid_email("first-last@example.com"))

    def test_percent_in_local(self):
        self.assertTrue(is_valid_email("user%tag@example.com"))

    def test_dot_in_local(self):
        self.assertTrue(is_valid_email("first.last@example.com"))

    def test_long_tld(self):
        self.assertTrue(is_valid_email("alice@example.museum"))

    def test_two_letter_tld(self):
        self.assertTrue(is_valid_email("alice@example.de"))

    def test_country_subdomain(self):
        self.assertTrue(is_valid_email("alice.bob+filter@mail.example.co.uk"))

    def test_numeric_local(self):
        self.assertTrue(is_valid_email("user_123@sub.domain.de"))

    def test_hyphen_in_domain(self):
        self.assertTrue(is_valid_email("alice@my-company.com"))

    def test_deep_subdomain(self):
        self.assertTrue(is_valid_email("a@a.b.c.de"))


class TestIsValidEmailInvalid(unittest.TestCase):
    """Ungültige Adressen – alle müssen False zurückgeben."""

    def test_empty_string(self):
        self.assertFalse(is_valid_email(""))

    def test_missing_at(self):
        self.assertFalse(is_valid_email("notanemail"))

    def test_missing_local_part(self):
        self.assertFalse(is_valid_email("@example.com"))

    def test_missing_domain(self):
        self.assertFalse(is_valid_email("alice@"))

    def test_missing_tld(self):
        self.assertFalse(is_valid_email("alice@example"))

    def test_tld_too_short(self):
        self.assertFalse(is_valid_email("alice@example.c"))

    def test_local_starts_with_dot(self):
        self.assertFalse(is_valid_email(".alice@example.com"))

    def test_local_ends_with_dot(self):
        self.assertFalse(is_valid_email("alice.@example.com"))

    def test_double_dot_in_local(self):
        self.assertFalse(is_valid_email("alice..bob@example.com"))

    def test_domain_starts_with_dot(self):
        self.assertFalse(is_valid_email("alice@.example.com"))

    def test_domain_starts_with_hyphen(self):
        self.assertFalse(is_valid_email("alice@-example.com"))

    def test_domain_ends_with_hyphen(self):
        self.assertFalse(is_valid_email("alice@example-.com"))

    def test_tld_contains_digit(self):
        self.assertFalse(is_valid_email("alice@example.c0m"))

    def test_double_at(self):
        self.assertFalse(is_valid_email("alice@@example.com"))

    def test_space_in_local(self):
        self.assertFalse(is_valid_email("ali ce@example.com"))

    def test_space_in_domain(self):
        self.assertFalse(is_valid_email("alice@exam ple.com"))


class TestIsValidEmailEdgeCases(unittest.TestCase):
    """Grenzfälle und Typ-Robustheit."""

    def test_none_input(self):
        self.assertFalse(is_valid_email(None))  # type: ignore[arg-type]

    def test_integer_input(self):
        self.assertFalse(is_valid_email(42))  # type: ignore[arg-type]

    def test_list_input(self):
        # type: ignore[arg-type]
        self.assertFalse(is_valid_email(["alice@example.com"]))

    def test_whitespace_only(self):
        self.assertFalse(is_valid_email("   "))

    def test_newline_in_address(self):
        self.assertFalse(is_valid_email("alice@exam\nple.com"))

    def test_tab_in_address(self):
        self.assertFalse(is_valid_email("alice@exam\tple.com"))

    def test_single_char_local(self):
        self.assertTrue(is_valid_email("a@example.com"))

    def test_single_char_domain_label(self):
        self.assertTrue(is_valid_email("alice@x.de"))

    def test_address_with_leading_whitespace(self):
        self.assertFalse(is_valid_email(" alice@example.com"))

    def test_address_with_trailing_whitespace(self):
        self.assertFalse(is_valid_email("alice@example.com "))

    def test_ip_literal_not_supported(self):
        # Quoted/IP-Literale bewusst nicht unterstützt
        self.assertFalse(is_valid_email("alice@[192.168.1.1]"))


if __name__ == "__main__":
    unittest.main()
