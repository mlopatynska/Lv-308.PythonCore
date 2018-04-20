
#z = [[2**x] for x in range(5)]
#print z


'''inp = raw_input("input word:\n")
x = [i for i in inp]
print x'''

#l = [i**3 for i in range(101) if i**3 > 100 ]
#print l


#[x+y for x in ['Python ','C '] for y in ['Language','Programming']]
#['Python Language', 'Python Programming', 'C Language', 'C Programming']


#l =[[i for i in range(10)] for j in range(10)]
#print l


#d = {i: [x for x in range(1,i) ] for i in range(10) }
#print(d)


d = {'name': 'Vasyl', 'surname': 'Bilan', 'id': '1', 'task': 'run application'}
for key in d:
    print ("student {} = {}".format(key, d[key]))

for key, val in d.iteritems():
    print ("{} = {} .".format(key, val))
for key in d.iterkeys():
    print ("student {} = {}".format(key, d[key]))
for val in d.itervalues():
    print ("student {} = {}".format("?", val))
