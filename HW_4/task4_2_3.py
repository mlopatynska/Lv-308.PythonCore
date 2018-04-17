flag = False
while not flag:
    row = input("How many rows are in your triangle?...\n")
    if isinstance(row, int) and row >= 1:
        flag = True
print("Half triangle")
for count in range(1, row+1):
    print("*" * count)
print("Full triangle")
for count in range(1, row+1):
    print(" " * (row-count) + "*" * (2*count -1) + " " * (row-count))
print("Inverted triangle")
for count in range(row, 0, -1):
    print(" " * (row-count) + "*" * (2*count -1) + " " * (row-count))
