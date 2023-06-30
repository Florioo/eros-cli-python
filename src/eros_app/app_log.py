import click
import time

from eros import Eros

@click.command()
@click.option('--channel', default=1, help='Channel to log')
@click.pass_context
def log(ctx,channel):
    # Check if the context is properly set
    if not ctx.obj.get('eros'):
        click.echo("No Eros object found",err=True)
        return False
    eros = ctx.obj['eros']
    
    click.echo(click.style(f"Starting the logger", fg='green'))

    eros.attach_channel_callback(channel, lambda data: print(data.decode(),end=""))
   
