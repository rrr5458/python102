numbers = [22, 1, 444, 33, 68, 66, 45, 33]
highest_number = numbers[0]
for number in numbers:
    if number > highest_number:
        highest_number = number

print(highest_number)

numbers = [22, 1, 444, 33, 68, 66]
lowest_number = numbers[0]
for number in numbers:
    if number < lowest_number:
        lowest_number = number

print(lowest_number)

