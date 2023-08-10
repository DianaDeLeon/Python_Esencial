import copy 

countries=['Mexico','Guatemala','Colombia','Argentina']
ages=[12,58,24,32]
receta=['Ensalada',2,'lechugas',5,'tomates']


print(id(countries))
print(countries)

countries[0]='Ecuador'
print(countries)

global_countries=countries
global_countries_copi=copy.copy(countries)
print(global_countries)

countries[0]='Honduras'

print(countries)
print(global_countries)
print(global_countries_copi)

for countri in countries:
    print(countri)