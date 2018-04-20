
space = 10
space_reverce = 1

print "_" * 20

for i in range(1, 20, 2):
    print i * '*'

print 'Half triangle'
print "_" * 20

for i in range(1,20 , 2):
    print " " * space + i * '*'
    space -= 1

print 'Full triangle'
print "_" * 20


for i in range(1, 20, 2):
    print " " * space_reverce + '*' * (20 -i)
    space_reverce += 1
print 'Inverted triangle'
