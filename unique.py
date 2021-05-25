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

if __name__ == "__main__":
    print is_unique("The quick brown fox jumps over the lazy dog")
    print is_unique("hello world!")
    print is_unique("aBcDeFgHiJkLmNoPqRsTuVwXyZ")
    print is_unique("The quick brown fx jmps v lazy dg")