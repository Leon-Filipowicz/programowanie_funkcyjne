def partition_list(lst, condition):
    true_list = [item for item in lst if condition(item)]
    false_list = [item for item in lst if not condition(item)]
    return true_list, false_list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers, odd_numbers = partition_list(numbers, lambda x: x % 2 == 0)
print("Liczby parzyste:", even_numbers)
print("Liczby nieparzyste:", odd_numbers)

greater_than_5, less_than_5 = partition_list(numbers, lambda x: x > 5)
print("Liczby większe od 5:", greater_than_5)
print("Liczby mniejsze od 5:", less_than_5)
