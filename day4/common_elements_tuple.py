tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

common = ()

for num in tuple1:
    if num in tuple2:
        common = common + (num,)

print("Common elements:", common)
