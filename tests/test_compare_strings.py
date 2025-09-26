import pytest
from compare_strings import expand_string, compare_strings

"""
Test suite for the compare_strings module.

This file validates the core string comparison algorithm by covering:
- Expansion of strings into counts, including handling of letters, digits, and special characters.
- Comparison of strings based on their expanded counts and letter content.
- Edge cases such as empty strings, strings with only digits or letters, and special characters.
- Case sensitivity in string comparison.
- Prefix logic when counts are equal, ensuring correct handling of partial matches.
- Scenarios where strings have the same count but different letters, or where digit expansion leads to different total counts.

Each test case documents the expected behavior for its scenario, including both typical and edge cases.
"""
class TestExpandString:
    def test_empty_string(self):
        assert expand_string("") == 0

    def test_only_letters(self):
        assert expand_string("abc") == 3
        assert expand_string("Hello") == 5

    def test_only_digits(self):
        assert expand_string("123") == 6  # 1+2+3
        assert expand_string("0") == 0

    def test_mixed(self):
        assert expand_string("a1b2") == 5  # a=1,1=1,b=1,2=2

    def test_special_chars(self):
        assert expand_string("a b!") == 2  # only 'a' and 'b'

class TestCompareStrings:
    def test_identical_strings(self):
        assert compare_strings("abc", "abc") == True

    def test_different_counts(self):
        assert compare_strings("a", "ab") == False  # 1 vs 2
        assert compare_strings("ab", "abc") == False  # 2 vs 3, different counts despite seeming like prefix

    def test_same_count_different_letters(self):
        assert compare_strings("ab", "cd") == False

    def test_prefix_match(self):
        # Only applies when counts are equal
        assert compare_strings("a1", "ab") == True  # count=2 for both, "ab".startswith("a") = True

    def test_empty_strings(self):
        assert compare_strings("", "") == True
        assert compare_strings("", "a") == False

    def test_digit_strings(self):
        assert compare_strings("1", "1") == True  # both count 1, no letters
        assert compare_strings("1", "2") == False  # 1 vs 2

    def test_mixed_with_digits(self):
        assert compare_strings("a1", "a2") == False  # 2 vs 3
        assert compare_strings("a1", "b1") == False  # both count 2, letters "a" and "b", not prefix

        # For "a1" letters "a", count 2
        # "b1" letters "b", count 2
        # len("a")=1 <= len("b")=1, "b".startswith("a") = False
        # else "a".startswith("b") = False
        # So False, which makes sense, different letters.

    def test_case_sensitivity(self):
        assert compare_strings("A", "a") == False