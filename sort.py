usr_input = input()

number_as_strings = usr_input.split()

sorted_numbers = []

for num_str in number_as_strings:
    num = int(num_str)
    sorted_numbers.append(num)

sorted_numbers.sort()

print(sorted_numbers)