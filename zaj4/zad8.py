def most_common_element(lst):
    if not lst:
        return None

    counter = {}
    for item in lst:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    max_count = max(counter.values())
    return [key for key, value in counter.items() if value == max_count]


data = [1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4]

print(most_common_element(data))
