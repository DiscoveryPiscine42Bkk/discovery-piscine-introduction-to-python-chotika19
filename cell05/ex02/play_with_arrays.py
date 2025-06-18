array = [2, 8, 9, 48, 8, 22, -12, 2]
new = set([x + 2 for x in array if x > 5])
print(array)
print(new)