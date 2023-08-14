import click

from clients.services import ClientService
from clients.models import  ClientModel


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
              type= str,
              prompt = True,
              help = 'The client name'
              )
@click.option('-c', '--company',
              type= str,
              prompt = True,
              help = 'The client company'
              )
@click.option('-e', '--email',
              type= str,
              prompt = True,
              help = 'The client email'
              )
@click.option('-p', '--position',
              type= str,
              prompt = True,
              help = 'The client position'
              )
@click.pass_context
def create (ctx, name, company, email, position):
    """ Crate s a new clients """
    client = ClientModel(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, cliente_uid):
    """Update a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, cliente_uid):
    """Deletes a client"""
    pass


all = clients

