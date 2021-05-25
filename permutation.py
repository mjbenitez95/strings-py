import utilities

def is_permutation(string_a, string_b):
    letters_a = utilities.get_letters(string_a)
    letters_b = utilities.get_letters(string_b)

    if len(letters_a) != len(letters_b):
        return False
    
    letters_a = sorted(letters_a)
    letters_b = sorted(letters_b)

    for i in range(len(letters_a)):
        if letters_a[i] != letters_b[i]:
            return False
    
    return True

if __name__ == "__main__":
    print is_permutation("tacocat", "aacctto")
    print is_permutation("abc def hi jklmn", "nml kj i hfed cb a")
    print is_permutation("lorem ipsum", "quick brown")
    print is_permutation("lorem", "fox")