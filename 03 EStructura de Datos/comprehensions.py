#Comprehensions  =  constructores qie nos permiten generar seciancias a partir de otras secuencias
#List comprehension
#Dictionary comprehension
#Set comprehension
import random

list_numbers=list(range(100))
print(list_numbers)

pares=[numero for numero in list_numbers if numero % 2 == 0]
print(pares)

student_uid=[1,2,3]
students=['Juan','Jose','Luisa']
students_whit_uid={uid: student for uid, student in zip(student_uid,students)}
print(students_whit_uid)

random_numbers=[]
for i in range(10):
    random_numbers.append(random.randint(1,5))

print(random_numbers)

non_repeated={number for number in random_numbers}

print (non_repeated)