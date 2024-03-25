def flatten_list(nested_list):
    flattened = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened.extend(flatten_list(sublist))
        else:
            flattened.append(sublist)
    return flattened


example_nested_list = [1, [2, 3], [4, [5, 6]], 7]
result = flatten_list(example_nested_list)
print(result)
