number = input()

digits = list(number)

digits.sort(reverse=True)

largest_num_str = ''.join(digits)

largest_num = int(largest_num_str)

print(largest_num)