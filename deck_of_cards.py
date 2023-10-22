cards = input().split(', ')
n = int(input())

for _ in range(n):
    command = input().split(', ')
    action = command[0]

    if action == "Add":
        card = command[1].strip()
        if card in cards:
            print("Card is already in the deck")
        else:
            cards.append(card)
            print("Card successfully added")
    elif action == "Remove":
        card = command[1].strip()
        if card in cards:
            cards.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        index = int(command[1])
        if 0 <= index < len(cards):
            removed_card = cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif action == "Insert":
        index = int(command[1])
        card = command[2].strip()
        if 0 <= index < len(cards):
            if card in cards:
                print("Card is already added")
            else:
                cards.insert(index, card)
                print("Card successfully added")
        else:
            print("Index out of range")

print(', '.join(cards))
