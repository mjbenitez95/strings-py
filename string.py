def is_even(num):
    return (num % 2 == 0)

def is_palindrome(some_string):
    letters = "".join(filter(str.isalpha, some_string.lower()))
    letter_counts = [0 for i in range(26)]
    
    for letter in letters:
        index = ord(letter) - ord("a")
        letter_counts[index] = 0 if letter_counts[index] else 1
        
    if is_even(len(letters)):
        return sum(letter_counts) == 0
    else:
        return sum(letter_counts) == 1

if __name__ == "__main__":
    print is_palindrome("Racecar")
    print is_palindrome("zzccbnddnbsbcaerq1qeracsb")
    print is_palindrome("Able was I ere I saw Elba")
    print is_palindrome("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod")
    print is_palindrome("T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt upset on drab pot toilet")