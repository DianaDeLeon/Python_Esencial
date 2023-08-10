#Itera a lo largo de una secuencia
print(range(10))

for i in range(10):
    print(i)

 #Itera mientras que se cumpla una condicion

def cuenta_regresiva(n):
    while n>0:
        print(n)
        n-=1

cuenta_regresiva(20)


def cuenta_regresiva2(n):
    while n>0:
        print(n)
        n+=0

#cuenta_regresiva2(20)