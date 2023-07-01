import click
from . import transport_selection
import logging

@click.group()
@click.option('--debug', is_flag=True, help='Enable debug mode')
def cli(debug):
    if debug:
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)-7s (%(msecs)6d) [%(name)s]: %(message)s')
    else:
        # disable logging
        logging.disable(logging.CRITICAL)

# Register the transport selection commands
cli.add_command(transport_selection.uart)
cli.add_command(transport_selection.udp)
cli.add_command(transport_selection.tcp)
cli.add_command(transport_selection.zmq)



if __name__ == '__main__':
    cli()