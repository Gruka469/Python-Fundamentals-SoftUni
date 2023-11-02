elements = input().split()
element_count = {}

for element in elements:
    element = element.lower()
    if element not in element_count:
        element_count[element] = 0
    element_count[element] += 1

result = []
for el, count in element_count.items():
    if count % 2 != 0:
        result.append(el)

print(*result, sep=" ")
