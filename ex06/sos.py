
import sys

MORSE_CODES = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def encode_morse(text):
    """Encode a string into Morse code."""
    assert isinstance(text, str), "the arguments are bad"
    assert all(char.upper() in MORSE_CODES for char in text), \
        "the arguments are bad"

    return ' '.join(MORSE_CODES[char.upper()] for char in text)


def main():
    """Read the command-line argument and print its Morse encoding."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        text = sys.argv[1]
        morse_text = encode_morse(text)
        print(morse_text)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
