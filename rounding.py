numbers = input().split()

rounded_numbers = [int(round(float(num))) for num in numbers]

print(rounded_numbers)