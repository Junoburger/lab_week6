import math

print("Enter an odd length string: ")
txt = str(input())

txtLength = len(txt)

if txtLength % 2 == 1:
    find_at_index = math.ceil(txtLength / 2) - 1
else:
    find_at_index = int(txtLength / 2) - 1

print("Middle character:", txt[find_at_index])
print("First half:", txt[:find_at_index])
print("Second half:", txt[find_at_index + 1:])
