#Decoradores = envuelven a otra funcion y permiten ejecutar codigo anres y despues que es llamada
PASSWORD='12345'


def password_required(func):
    def wrapper():
        password=input('What is your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('The passwod is not correct')
    return wrapper

@password_required   #Permite ejecutar logica antes y despues de la funcion
def needs_password():
    print("The password is correct")



def upperName(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return result.upper()
    
    return wrapper

@upperName
def say_my_name(name):
    return ('Hola, {}'.format(name))


if __name__ == '__main__':
 #   needs_password()
 print(say_my_name('Diana'))