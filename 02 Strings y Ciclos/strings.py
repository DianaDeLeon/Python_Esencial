country='Colombia'

print(country[1])

print(len(country))

second_letter=country[1]

print(id(second_letter))

other_var='o'
print(id(other_var))

#Al modificar una cadena asigna un nuevo espacio en memoria
country+='no'
print(id(country))

#OPERACIONES CON STRINGS
# upper,lower,find,startswith,endswith,capitalize

#Operadores de pertenencia
# in, not in

print('-'*50)
platzi='platzi'

print(platzi.upper()) #Mayusculas
print(platzi.startswith('p')) #Si inicia con la letra

#print(dir(platzi))

