coffees = input().split()
n = int(input())

for _ in range(n):
    command = input().split()
    
    if command[0] == "Include":
        coffee = command[1]
        coffees.append(coffee)
    elif command[0] == "Remove":
        direction = command[1]
        count = int(command[2])
        if direction == "first":
            coffees = coffees[count:]
        elif direction == "last":
            coffees = coffees[:-count]
    elif command[0] == "Prefer":
        index1 = int(command[1])
        index2 = int(command[2])
        if 0 <= index1 < len(coffees) and 0 <= index2 < len(coffees):
            coffees[index1], coffees[index2] = coffees[index2], coffees[index1]
    elif command[0] == "Reverse":
        coffees = coffees[::-1]

print(f"Coffees: \n{' '.join(coffees)}")
