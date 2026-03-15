numbers = [10, 20, 30, 20, 40, 10, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique)
