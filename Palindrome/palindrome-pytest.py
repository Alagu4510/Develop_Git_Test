import re

class PalindromeChecker:
    """This class checks if a string is a palindrome.

    Attributes:
        value (str): The string to be checked.

    Methods:
        is_palindrome(self): Checks if the string is a palindrome.
    """

    def __init__(self, value: str) -> None:
        """Initializes the PalindromeChecker object.

        Args:
            value (str): The string to be checked.
        """
        self.value = value

    def is_palindrome(self) -> bool:
        """Checks if the string is a palindrome.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        try:
            self.value = self.value.lower()
            self.value = re.sub(r"[^a-zA-Z0-9]", "", self.value)
            rev_value = self.value[::-1]
        except AttributeError:
            raise ValueError("Please enter a string")

        return self.value == rev_value


def main() -> None:
    value = input("Enter a Value: ")
    checker = PalindromeChecker(value)

    if checker.is_palindrome():
        print("Is a Palindrome")

    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()


import pytest


@pytest.mark.parametrize("value", ["amma", "Madam", "1234321","Malayalam","Madam,I'm Adam!!"])
def test_is_palindrome(value):
    checker = PalindromeChecker(value)
    assert checker.is_palindrome() is True


@pytest.mark.parametrize("value", ["hai", "world", "12345"])
def test_is_not_palindrome(value):
    checker = PalindromeChecker(value)
    assert checker.is_palindrome() is False



#   PEP8 rules
# - Use 4 spaces for indentation
# - Limit all lines to a maximum of 79 characters
# - Use lowercase for function and variable names
# - Use double quotes for strings
# - Add docstrings to all functions
