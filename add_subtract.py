def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    final_result = subtract(result, c)
    return final_result



num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))