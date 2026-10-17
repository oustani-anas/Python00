
import sys


def is_punctuation(char):
    """Check whether a character is a punctuation mark."""
    return char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def count_characters(text):
    """Count and display the different types of characters."""
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif is_punctuation(char):
            punctuation_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    total_characters = len(text)

    print(f"The text contains {total_characters} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """Read the input and count its characters."""
    try:
        assert len(sys.argv) <= 2, \
            "more than one argument is provided"

        if len(sys.argv) == 1 or sys.argv[1] == "":
            text = input("What is the text to count?\n")
            text += "\n"
        else:
            text = sys.argv[1]

        count_characters(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
