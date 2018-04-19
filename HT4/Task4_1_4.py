
cub_numb = list(raw_input("Enter any number: "))
sum_numb = 0

for count in cub_numb:
    sum_cub = int(count)**3
    sum_numb += sum_cub
# It's loop counting summary of cube from every number

print 'The summary of cubs number {} is' \
      ' {}'.format(''.join(cub_numb), sum_numb)
