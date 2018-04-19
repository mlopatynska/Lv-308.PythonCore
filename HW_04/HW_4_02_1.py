myList = input('Enter list of numbers: ').split()
theSmallest = float(myList[0])
for element in myList:
    if theSmallest > float(element):
       theSmallest = float(element)
print(f'{theSmallest} is a minimal element')
