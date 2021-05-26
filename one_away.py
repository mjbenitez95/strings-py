import utilities

def one_away(string_a, string_b):
    if(abs(len(string_a) - len(string_b) > 1)):
        return False

    letters_a = utilities.get_letters(string_a)
    letters_b = utilities.get_letters(string_b)

    letter_counts_a = utilities.get_letter_counts(letters_a)
    letter_counts_b = utilities.get_letter_counts(letters_b)

    return letters_a == letters_b

if __name__ == "__main__":
    print one_away("matthew", "Matthew")

