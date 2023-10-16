# numbers = [int(number) for number in input().split()]
# removing_indexes = input().split()
# removed_elements = []

# for i in removing_indexes:
#     if i.isdigit():
#         index_to_remove = int(i)

#         if index_to_remove < len(numbers):
#             removed_element = numbers.pop(index_to_remove)
#             removed_elements.append(removed_element)

#         elif index_to_remove <= 0:
#             removed_element = numbers.pop(0)
#             numbers[-1] = numbers[0]
#             removed_elements.append(removed_element)

#         elif index_to_remove > len(numbers):
#             removed_element = numbers.pop(-1)
#             numbers[0] = numbers[-1]
#             removed_elements.append(removed_element)

#         else:
#             numbers <= 0
#             break

#         for j in range(len(numbers)):
#             if numbers[j] <= removed_element:
#                     numbers[j] += removed_element
#             else:
#                     numbers[j] -= removed_element

#         for num in numbers:
#             if num <= removed_element:
#                 num += removed_element
#             elif num > removed_element:
#                 num -= removed_element
# summed_removed_elements = sum(removed_elements)
# print(summed_removed_elements)

def increment_decrement(control_num: int, sequence: list) -> None:
    for index in range(len(sequence)):
        if sequence[index] <= control_num:
            sequence[index] += control_num
        else:
            sequence[index] -= control_num


removed_elements_sum = 0
number_sequence = [int(i) for i in input().split()]

while number_sequence:
    index_to_remove = int(input())
    if index_to_remove < 0:
        removed_element = number_sequence[0]
        number_sequence[0] = number_sequence[-1]
    elif index_to_remove >= len(number_sequence):
        removed_element = number_sequence[-1]
        number_sequence[-1] = number_sequence[0]
    else:
        removed_element = number_sequence.pop(index_to_remove)

    removed_elements_sum += removed_element
    increment_decrement(removed_element, number_sequence)

print(removed_elements_sum)