text = input()
unique_symbols = ""
repetitions = 0
current_symbol = ""

for index in range(len(text)):
    if text[index].isdigit():
        current_symbol += text[index]
    else:
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        repetitions = int(repetitions)
        unique_symbols += current_symbol * repetitions
print(unique_symbols)