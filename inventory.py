journal = input().split(", ")

def collect(item):
    if item not in journal:
        journal.append(item)

def drop(item_to_remove):
    if item_to_remove in journal:
        journal.remove(item_to_remove)

def combine_items(old_item, new_item):
    if old_item in journal:
        index = journal.index(old_item)
        journal.insert(index + 1, new_item)

def renew_item(item):
    if item in journal:
        journal.remove(item)
        journal.append(item)
     

while True:
    command = input()
    if command == "Craft!":
        break

    action, *args = command.split(" - ")

    if action == "Collect":
        collect(args[0])
    elif action == "Drop":
        drop(args[0])
    elif action == "Combine Items":
        old, new = args[0].split(":")
        combine_items(old, new)
    elif action == "Renew":
        renew_item(args[0])

print(", ".join(journal))
