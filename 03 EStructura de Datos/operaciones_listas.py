# Añadir un elemento al final de la lista append
# Eliminar el ultimo elemento de la lista pop, del, remove
# Ordenar una lista de mayor a menor sort
import random

a=list(range(0,50,2)) # Lista de numero pares
b=list(range(0,10))

print(a+b)
print(b*2)

fruits=list()
# es lo mismo que fruits=[]

fruits.append('apple')
print(fruits)

fruits.append('banana')
print(fruits)

fruits.append('kiwi')
print(fruits)

some_fruit=fruits.pop()
print(some_fruit)
print(fruits)

some_fruit=fruits.pop(0)
print(some_fruit)
print(fruits)

del fruits[0]
print(fruits)


ramdom_numbers=[]

for i in range(10):
    ramdom_numbers.append(random.randint(0,15))

print(ramdom_numbers)

#ramdom_numbers.sort()
order_numbers=sorted(ramdom_numbers)
print(order_numbers)