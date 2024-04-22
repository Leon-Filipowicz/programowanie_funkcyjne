def even_numbers(nmbrs):
    for number in nmbrs:
        if number % 2 == 0:
            result.append(number)


numbers = [1, 2, 3, 4, 5, 6]
result = []

even_numbers(numbers)

print(result)

area = lambda lenght, width: lenght * width
lenght = 2
width = 5

rectangle_area = area(lenght, width)
print(f'Pole = {rectangle_area}')
