#NO podemos modificar las tuplas
a=1,2,3
print(type(a))

a=(1,2,3)
print((a[0]))

a=(1,1,1,2,3)

#print(dir(a))

print(a.count(2))
print(a.count(1))
print(a.index(1))
print(a.index(3))


c=set([1,2,3])
d={3,4,5}

#Los sets no pueden tener duplicados
c.add(30)
print(c)

print(c.intersection(d))
print(c.union(d))
print(c.difference(d))
print(c.remove(30))
print(c)