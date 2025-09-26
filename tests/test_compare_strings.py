import pytest
from compare_strings import parse_string, compare_strings

# Test suite for the compare-strings functionality
# This file validates the core string comparison algorithm

class TestParseString:
    def test_no_count(self):
        assert parse_string("abc") == ("abc", 3)
        assert parse_string("") == ("", 0)

    def test_with_count(self):
        assert parse_string("abc13") == ("abc1", 7)  # "abc" + "1" + 3 missing = "abc1" + 3 chars

    def test_single_digit_no_count(self):
        assert parse_string("a1") == ("a1", 2)  # No count, exact match expected

class TestCompareStrings:
    def test_exact_match(self):
        assert compare_strings("abc", "abc") == True

    def test_count_match(self):
        assert compare_strings("abc1234", "abc13") == True  # "abc1" + 3 chars = "abc1234"

    def test_count_no_match_length(self):
        assert compare_strings("abc12", "abc13") == False  # "abc12" is 5 chars, expected 7

    def test_count_no_match_prefix(self):
        assert compare_strings("def1234", "abc13") == False  # Wrong prefix

    def test_no_count_exact_match(self):
        assert compare_strings("a1", "a1") == True

    def test_no_count_different(self):
        assert compare_strings("a1", "a2") == False

    def test_empty_strings(self):
        assert compare_strings("", "") == True

    def test_empty_vs_nonempty(self):
        assert compare_strings("", "abc13") == False