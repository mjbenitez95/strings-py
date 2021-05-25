import utilities

def compress(some_string):
    compressed = ""
    letter_counts = [0 for i in range(26)]

    letters = utilities.get_letters(some_string)

    for char in letters:
        index = utilities.get_letter_index(char)
        letter_counts[index] += 1

    for index, count in enumerate(letter_counts):
        if count:
            compressed += chr(index + ord("a")).lower()
            if count > 1:
                compressed += str(count)

    return compressed

if __name__ == "__main__":
    print "--Compression--"
    print compress("matthew") == "aehmt2w"
    print compress("the quick brown fox jumps over the lazy dog") == "abcde3fgh2ijklmno4pqr2st2u2vwxyz"
    print compress("zyxwvutsrqponmlkjihgfedcba") == "abcdefghijklmnopqrstuvwxyz"
