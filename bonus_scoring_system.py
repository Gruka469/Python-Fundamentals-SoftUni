import math
 
number_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())
 
total_bonus = 0
scores_list = []
 
if number_lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
 
else:
    for lectures in range(1, number_students + 1):
        attendance = int(input())
        scores_list.append(attendance)
 
    total_bonus = (max(scores_list) / number_lectures) * (5 + additional_bonus)
 
    print(f'Max Bonus: {math.ceil(total_bonus)}.')
    print(f'The student has attended {max(scores_list)} lectures.')