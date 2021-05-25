def get_letters(some_string):
    letters = "".join(filter(str.isalpha, some_string.lower()))
    return letters

def get_letter_index(char):
    index = ord(char) - ord("a")
    return index
