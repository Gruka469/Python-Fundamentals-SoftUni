def decipher_word(word):
    result = []
    i = 0
    while i < len(word):
        if word[i].isdigit():
            code = ""
            while i < len(word) and word[i].isdigit():
                code += word[i]
                i += 1
            result.append(chr(int(code)))
        else:
            result.append(word[i])
            i += 1

    if len(result) > 2:
        result[1], result[-1] = result[-1], result[1]

    return ''.join(result)

def decipher_message(secret_message):
    words = secret_message.split()
    deciphered_words = [decipher_word(word) for word in words]
    return " ".join(deciphered_words)

secret_message = input()
deciphered_message = decipher_message(secret_message)
print(deciphered_message)
