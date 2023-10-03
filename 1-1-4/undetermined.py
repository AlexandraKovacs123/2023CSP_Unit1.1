i = int(input("enter number:"))
while (i >= 0):
    # add a nested loop that decrements the value by 1
    # until it is only one again
    while (i > 1):
        i = i - 1
    i = i + 1
print(i)
