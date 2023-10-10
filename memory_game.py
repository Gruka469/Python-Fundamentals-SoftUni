user_input = input()
my_list = []

integers = user_input.split()
my_list.extend(map(int, integers))

list_average = sum(my_list) / len(my_list)

greater_than_average = [num for num in my_list if num > list_average]

greater_than_average.sort(reverse=True)

if greater_than_average:
    top_5 = greater_than_average[:5]
    print(*top_5)
else:
    print("No")