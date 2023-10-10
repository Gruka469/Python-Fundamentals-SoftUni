people_queue = int(input())
lift_state = input().split()
wagons = [int(capacity) for capacity in lift_state]
max_wagons = len(wagons)

for person in range(people_queue):
    placed = False
    for i in range(len(wagons)):
        if wagons[i] < 4:
            wagons[i] += 1
            placed = True
            break

    if not placed and len(wagons) < max_wagons:
        wagons.append(1)

total_people_on_lift = sum(wagons)
empty_spots = 4 * max_wagons - total_people_on_lift

if empty_spots > 0:
    print(f"The lift has empty spots!\n{' '.join(map(str, wagons))}")
elif people_queue > total_people_on_lift:
    print(f"There isn't enough space! {people_queue - total_people_on_lift} people in a queue!\n{' '.join(map(str, wagons))}")
else:
    print(' '.join(map(str, wagons)))
