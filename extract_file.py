filepath = input().split("\\")
filname_and_extension = filepath[-1]
filename, extension = filname_and_extension.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
