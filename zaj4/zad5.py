def split_list_to_chunks(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 3

print(split_list_to_chunks(data, size))
