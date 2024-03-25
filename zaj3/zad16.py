def remove_whitespace(strings):
    return [string.replace(" ", "") for string in strings]


strings_example = ["   Hello ", "World ", "   Python   "]
print(remove_whitespace(strings_example))
