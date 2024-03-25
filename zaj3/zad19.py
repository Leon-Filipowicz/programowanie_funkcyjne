def check_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


example1 = "listen"
example2 = "silent"
print(check_anagrams(example1, example2))
