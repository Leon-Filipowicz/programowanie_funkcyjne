def merge_dictionaries(*dictionary):
    result = {}
    for d in dictionary:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result


dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 3, 'c': 4}

print(merge_dictionaries(dict1, dict2))
