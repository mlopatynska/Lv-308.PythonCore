def selection_sort(mas, x):
  for p in range(len(mas) - 1):
    i = find_x(mas[p:], x, 1, 0, len(mas) - p)
    i += p
    mas[p], mas[i] = mas[i], mas[p]

x = [10, 3, 8 ,5, 9, 7, 12]

print(selection_sort(x))
