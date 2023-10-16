# input_string = input()

# numbers = input_string.split(", ")

# even_indices = []

# for index, number in enumerate(numbers):
#     if int(number) % 2 == 0:
#         even_indices.append(index)

# if even_indices:
#     print(even_indices)

def condition(x): return x % 2 == 0


number_list = [int(i) for i in input().split(", ")]
even_list = [i for i in range(len(number_list)) if condition(number_list[i])]
print(even_list)