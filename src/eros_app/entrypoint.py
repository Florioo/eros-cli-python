import click
from . import transport_selection
    
@click.group()
def cli():
    pass

# Register the transport selection commands
cli.add_command(transport_selection.uart)
cli.add_command(transport_selection.udp)
cli.add_command(transport_selection.tcp)
cli.add_command(transport_selection.zmq)

if __name__ == '__main__':
    cli()