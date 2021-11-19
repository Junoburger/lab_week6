char = input("Enter a character: ")


if (char.isnumeric() is False and char.isalpha() is False):
    print(char, "is a non-alphanumeric character.")

if (char.isnumeric() and char.isalpha() is False):
    print(char, "is  a digit.")

if (char == char.upper() and char.isalpha() is True):
    print(char, "is an upper case letter.")

if (char == char.lower() and char.isalpha() is True):
    print(char, "is a lower case letter.")
