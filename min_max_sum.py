usr_input = input()

split_usr_input = usr_input.split()
min_max_sum = []

for num_str in split_usr_input:
    num = int(num_str)
    min_max_sum.append(num)

print(f"The minimum number is {min(min_max_sum)}")
print(f"The maximum number is {max(min_max_sum)}")
print(f"The sum number is: {sum(min_max_sum)}")
