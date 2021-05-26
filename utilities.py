def get_letters(some_string):
    letters = "".join(filter(str.isalpha, some_string.lower()))
    return letters

def get_letter_index(char):
    index = ord(char) - ord("a")
    return index

def get_letter_counts(letters):
    letter_counts = [0 for i in range(26)]
    for character in letters:
        letter_counts[get_letter_index(character)] += 1

    return letter_counts