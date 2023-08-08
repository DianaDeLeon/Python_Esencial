#Suma
suma =20+4

#Resta
resta =20-4

#Multiplicacion
multiplicacion =20*4

#Division (// division entera)
division =20/4
entera =20//4

#Mod
mod =20%4


print('Suma:',suma)
print('Resta',resta)
print('Division:',division, ' Exacta:',entera)
print('Multiplicacion',multiplicacion)
print('Mod',mod)

#Tipo 
print(type(50))
print(type("Hola"))

#Asignacion
a=5
b=5

a+=3
b*=3
print(a,' ',b)

#Operadores Logicos
x=2
y=3
a=5
b=7

print((x<y) and (a<b))
print((x<y) and (a>b))
print((x<y) or (a>b))

if x<y:
    print('x es menor que y')
else:
    print('x no es menor que y')