# compare-strings

[![CI](https://github.com/LeoncioXavier/compare-strings/actions/workflows/ci.yml/badge.svg)](https://github.com/LeoncioXavier/compare-strings/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/LeoncioXavier/compare-strings/branch/main/graph/badge.svg)](https://codecov.io/gh/LeoncioXavier/compare-strings)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sophisticated string comparison utility that implements a unique algorithm for determining string "equivalence" based on character expansion and sequence matching. Unlike standard string comparison, this tool considers letters as having equal weight while digits contribute their numeric values, enabling creative matching scenarios for text processing and analysis.

## Features

- **Custom Comparison Logic**: Letters count as 1, digits add their numeric value
- **Sequence Validation**: Checks for prefix relationships when expansion values match
- **Command-line Interface**: Easy-to-use CLI for quick comparisons
- **Python Library**: Import and use in your Python projects
- **Comprehensive Testing**: Full test coverage with edge case handling

## Setup

Clone the repository and set up a Python virtual environment:

```bash
git clone https://github.com/LeoncioXavier/compare-strings.git
cd compare-strings
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

## Usage

After setting up the virtual environment, activate it and run the script:

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
compare-strings "string1" "string2"
```

Or use it as a module in Python:

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
compare-strings "ab" "abc"   # False (2 vs 3)

# Prefix match (same count, one letter sequence is prefix of the other)
compare-strings "a1" "ab"    # True (count=2, letters="a" vs "ab")

# Digit expansion differences
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
