import sys

def expand_string(s):
    # This function calculates the total character count
    # Letters count as 1 each, numbers add to the total count
    total_chars = 0

    for char in s:
        if char.isdigit():
            total_chars += int(char)
        elif char.isalpha():
            total_chars += 1

    return total_chars

def compare_strings(str1, str2):
    count1 = expand_string(str1)
    count2 = expand_string(str2)

    # First validation: check if character counts are the same
    if count1 != count2:
        return False

    # Second validation: check if existing letters are the same in same order
    # Extract only the letters from each string (preserve order)
    letters1 = ''.join([char for char in str1 if char.isalpha()])
    letters2 = ''.join([char for char in str2 if char.isalpha()])

    # Check if one is a prefix of the other (or they are equal)
    if len(letters1) <= len(letters2):
        return letters2.startswith(letters1)
    else:
        return letters1.startswith(letters2)

def main():
    if len(sys.argv) != 3:
        print("Usage: python -m compare_strings <string1> <string2>")
        sys.exit(1)

    string1 = sys.argv[1]
    string2 = sys.argv[2]

    if compare_strings(string1, string2):
        print("The strings are considered the same.")
    else:
        print("The strings are different.")

if __name__ == "__main__":
    main()