list_orig = [5, 6, "e", "t", 5, "e", 2]
list_new = []

for item in list_orig:
    if item not in list_new:
        list_new.append(item)
print(list_new)