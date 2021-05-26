def urlify(some_string):
    return some_string.replace(" ", "%20")

def urlify_by_iteration(some_string, length):
    url, non_spaces = "", ""
    non_spaces = ""
    for i in range(length, -1, -1):
        if some_string[i] != " ":
            non_spaces = some_string[i] + non_spaces
        else:
            url = "%20" + non_spaces + url
            non_spaces = ""
    url = non_spaces + url
    return url

if __name__ == "__main__":
    print urlify("Mr John Smith")
    print urlify("the quick brown fox jumps over the lazy dog")

    print urlify_by_iteration("Mr John Smith    ", 13)
    print urlify_by_iteration("the quick brown fox jumps over the lazy dog", 42)
