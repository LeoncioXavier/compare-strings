# compare-strings

[![CI](https://github.com/LeoncioXavier/compare-strings/actions/workflows/ci.yml/badge.svg)](https://github.com/LeoncioXavier/compare-strings/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/LeoncioXavier/compare-strings/branch/main/graph/badge.svg)](https://codecov.io/gh/LeoncioXavier/compare-strings)
[![PyPI version](https://badge.fury.io/py/compare-strings.svg)](https://pypi.org/project/compare-strings/)
[![PyPI downloads](https://img.shields.io/pypi/dm/compare-strings.svg)](https://pypi.org/project/compare-strings/)
[![Python versions](https://img.shields.io/pypi/pyversions/compare-strings.svg)](https://pypi.org/project/compare-strings/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A custom string comparison tool that expands strings based on letter and digit values.

## Installation

```bash
pip install compare-strings
```

Or from source:

```bash
git clone https://github.com/LeoncioXavier/compare-strings.git
cd compare-strings
pip install -e .
```

## Usage

```bash
compare-strings "string1" "string2"
```

Or as a module:

```python
from compare_strings import compare_strings

result = compare_strings("hello", "hello")
print(result)  # True
```

## How it works

The comparison algorithm:

1. **Expansion**: Each letter counts as 1, each digit adds its numeric value
2. **Count Comparison**: Total expanded values must be equal
3. **Letter Sequence Check**: If counts match, check if one letter sequence is a prefix of the other

### Examples

```bash
# Same strings
compare-strings "abc" "abc"  # True

# Different counts
compare-strings "a" "ab"     # False (1 vs 2)

# Prefix match
compare-strings "ab" "abc"   # True

# Digit expansion
compare-strings "a1" "b2"    # False (2 vs 3)
```

## Development

### Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### Running tests

```bash
pytest
```

### Test Coverage

The test suite includes comprehensive coverage of all functionality:

#### `TestExpandString`
- **Empty strings**: Verifies correct handling of empty input
- **Letter-only strings**: Tests basic letter counting
- **Digit-only strings**: Validates digit value summation
- **Mixed alphanumeric**: Tests combination of letters and digits
- **Special characters**: Ensures non-alphanumeric characters are ignored

#### `TestCompareStrings`
- **Identical strings**: Confirms exact matches return True
- **Different counts**: Validates count mismatch detection
- **Same count, different letters**: Tests letter sequence comparison
- **Prefix matching**: Verifies prefix logic for strings with same expanded count
- **Empty string handling**: Tests edge cases with empty inputs
- **Digit-only comparisons**: Checks behavior with numeric-only strings
- **Mixed content**: Tests complex combinations of letters and digits
- **Case sensitivity**: Confirms case-sensitive comparison behavior

#### Test Statistics
- **Total tests**: 13 test cases
- **Coverage**: >95% code coverage
- **CI Integration**: Automated testing on Python 3.8-3.12

Run tests with coverage reporting:

```bash
pytest --cov=src/compare_strings --cov-report=html
```

View detailed coverage report in `htmlcov/index.html`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) for details.

## Documentation

See [PRD.md](PRD.md) for detailed product requirements and edge case analysis.
