def compress(some_string):
    compressed = ""
    letter_counts = [0 for i in range(26)]

    letters = "".join(filter(str.isalpha, some_string.lower()))

    for char in letters:
        index = ord(char) - ord("a")
        letter_counts[index] += 1

    for index, count in enumerate(letter_counts):
        if count:
            compressed += chr(index + ord("a")).lower()
            if count > 1:
                compressed += str(count)

    return compressed
        
if __name__ == "__main__":
    print compress("matthew")
    print compress("the quick brown fox jumps over the lazy dog")