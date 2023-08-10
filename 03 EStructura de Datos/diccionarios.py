rae={}

rae['pizza']='La comida mas deliciosa del mundo'
print(rae)

rae['pasta']='La comida mas sabrosa de italia'
print(rae)

print(rae['pizza'])

a=rae.get('helado',None)
print(a)

print(rae.keys())

print(rae.values())

print(rae.items())


for key in rae.values():
    print(key)