def is_palinfrom(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check:")
if is_palinfrom(word):
    print(f"'{word}' is a palindrom")
else:
    print(f"'{word}' is not a palindrom")