input_string = input()

string_list = input_string.split()

opposite_number = []
for number in string_list:
    current_number = -int(number)
    opposite_number.append(current_number)
print(opposite_number)