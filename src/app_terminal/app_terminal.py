
from eros import Eros, ErosSerial,ErosUDP,ErosTCP
import time
import click

@click.group()
def cli():
    pass


@cli.command()
def uart():
    click.echo('Running UART')
