import math

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

aprons_needed = math.ceil(students * 1.2)

total_cost = (flour_price * students) + (egg_price * students * 10) + (apron_price * aprons_needed)

free_flour_packages = students // 5

total_cost -= (free_flour_packages * flour_price)

if total_cost <= budget:
    print(f'Items purchased for {total_cost:.2f}$.')
else:
    needed_money = total_cost - budget
    print(f'{needed_money:.2f}$ more needed.')
