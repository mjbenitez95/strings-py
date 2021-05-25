def is_unique(some_string):
    letters = "".join(filter(str.isalpha, some_string.lower()))
    if len(letters) > 26:
        return False

    letter_counts = [False for i in range(26)]

    for letter in letters:
        index = ord(letter) - ord("a")
        if letter_counts[index]:
            return False
        else:
            letter_counts[index] = True

    return True

def is_unique_no_extra_space(some_string):
    letters = "".join(filter(str.isalpha, some_string.lower()))
    if len(letters) > 26:
        return False

    letters = sorted(letters)
    for index in range(len(letters) - 1):
        if letters[index] == letters[index + 1]:
            return False
    return True

if __name__ == "__main__":
    print is_unique("The quick brown fox jumps over the lazy dog")
    print is_unique("hello world!")
    print is_unique("aBcDeFgHiJkLmNoPqRsTuVwXyZ")
    print is_unique("The quick brown fx jmps v lazy dg")
    print ""
    print is_unique_no_extra_space("The quick brown fox jumps over the lazy dog")
    print is_unique_no_extra_space("hello world!")
    print is_unique_no_extra_space("aBcDeFgHiJkLmNoPqRsTuVwXyZ")
    print is_unique_no_extra_space("The quick brown fx jmps v lazy dg")