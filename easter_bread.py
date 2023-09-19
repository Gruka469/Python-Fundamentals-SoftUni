budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
milk_liter_price = price_kg_flour * 1.25
easter_bread_recipe_price = price_kg_flour + price_pack_eggs + (milk_liter_price * 0.25)

colored_egg_count = 0
loaves_count = 0
current_budget = budget

while current_budget >= easter_bread_recipe_price:
    loaves_count += 1
    colored_egg_count += 3

    if loaves_count % 3 == 0:
        lost_eggs = (loaves_count - 2)
        colored_egg_count -= lost_eggs

    current_budget -= easter_bread_recipe_price

formatted_money_left = "{:.2f}".format(current_budget)

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_egg_count} eggs and {formatted_money_left}BGN left.")

