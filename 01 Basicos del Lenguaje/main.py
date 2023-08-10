import sys

clients=[
    {
        'name':'Pablo',
        'company':'Google',
        'email':'pablo@gamil.com',
        'position':'Software engineer'
    },
    {
        'name':'Maria',
        'company':'Facebook',
        'email':'maria@gamil.com',
        'position':'Data engineer'
    }
]


def create_cliente(client):
    global clients

    if client not in clients:
        clients.append(client)  
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx,client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def update_client(client,client_new):
    global clients
    if 0 <= client < len(clients):
        clients[client] = client_new
        print(f'Client at index {client} has been updated.')
    else:
        print('Invalid index.')


def search_client(index):
    global clients

    if 0 <= index < len(clients):
        return True
    else:
        return False


def delete_client(index):
    global clients

    if 0 <= index < len(clients):
        removed_client = clients.pop(index)
        print(f'Client {removed_client["name"]} has been removed.')
    else:
        print('Invalid index.')



def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]erach client')
    

def _get_client_field(field_name):
    field=None

    while not field:
        field=input('What is the client {}?'.format(field_name))

    return field


def _get_client_name():
    client_name=None

    while not client_name:
        client_name=input('What is the client name? ')

        if client_name=='exit':
            client_name=None
            break

    if not client_name:
        sys.exit()

    return client_name

#Aqui comienza
if __name__=='__main__':
    _print_welcome()

    command=input()
    command=command.upper()

    if command=='C':
        client={
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'email':_get_client_field('email'),
            'position':_get_client_field('position'),
        }
        create_cliente(client)
        list_clients()
    if command=='L':
        list_clients()
    elif command =='D':
        client=int(input('What is the client id? '))
        delete_client(client)
        list_clients()
    elif command =='U':
        client=int(input('What is the client id? '))
        print('Type new data: ')
        client_new={
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'email':_get_client_field('email'),
            'position':_get_client_field('position'),
        }
        update_client(client,client_new)
        list_clients()
    elif command == 'S':
        client=int(input('What is the client id? '))
        found = search_client(client)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list '.format(client)) 
else:
    print('Invalid Command')    
