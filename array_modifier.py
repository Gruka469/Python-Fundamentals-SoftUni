my_list = []
user_input = input()

def swap():
    if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):
        my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def multiplication():
    if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):
        my_list[index1] * my_list[index2]

def decrease():
    for num in range(len(my_list)):
        my_list[num] -= 1

while True:
    command = input()
    if command == "end":
        break
    
    command_parts = command.split()
    action = command_parts[0]
    
    if action == "swap":
        index1, index2 = map(int, command_parts[1:])
        swap(index1, index2)
    elif action == "multiply":
        index1, index2 = map(int, command_parts[1:])
        multiplication(index1, index2)
    elif action == "decrease":
        decrease()

print(", ".join(map(str, my_list)))



# my_list = [int(num) for num in input().split()]

# while True:
#     command = input()
    
#     if command == "end":
#         break
    
#     command_parts = command.split()
#     action = command_parts[0]
    
#     if action == "swap":
#         index1, index2 = map(int, command_parts[1:])
#         if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):
#             my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
#     elif action == "multiply":
#         index1, index2 = map(int, command_parts[1:])
#         if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):
#             my_list[index1] = my_list[index1] * my_list[index2]
#     elif action == "decrease":
#         my_list = [num - 1 for num in my_list]

# print(", ".join(map(str, my_list)))
