import click
from eros_core import Eros
from .decorators import eros_check

@click.command(name="log", help="Log the data of a specific channel")
@click.pass_context
@eros_check
@click.option('--channel', default=1, help='Channel to log')
def app_log(ctx,channel):
    eros = ctx.obj.get('eros')
    click.echo(click.style(f"Starting the logger", fg='green'))
    eros.attach_channel_callback(channel, lambda data: print(data.decode(),end=""))
   
