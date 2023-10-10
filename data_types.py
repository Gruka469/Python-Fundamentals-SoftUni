def process_data(data_type, data):
    if data_type == 'int':
        result = int(data) * 2
    elif data_type == 'real':
        result = '{:.2f}'.format(float(data) * 1.5)
    elif data_type == 'string':
        result = f"${data}$"
    return result

data_type = input()
data = input()

result = process_data(data_type, data)
print(result)
