numbers = [22, 1, 444, 33, 68, 66, 45, 33]

even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else: 
        odd_numbers.append(num)

print(even_numbers)
print(odd_numbers)