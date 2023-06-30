import click
import time
import threading
from eros import Eros
from .eros_terminal import ErosTerminal

@click.command()
@click.option('--main_channel', default=5, help='Main Channel to connect to')
@click.option('--aux_channel', default=6, help='Aux Channel to connect to')
# Monitor channels 
@click.option('--monitor_channel', default=None,type=int, help='Monitor Channels to connect to')
@click.pass_context
def cli(ctx, main_channel, aux_channel, monitor_channel):
    # Check if the context is properly set
    if not ctx.obj.get('eros'):
        click.echo("No Eros object found",err=True)
        return False
    
    eros = ctx.obj['eros']
    
    # Create the terminal
    terminal = ErosTerminal(eros, main_channel, aux_channel)
    
    
    if monitor_channel:
        terminal.enable_monitor(monitor_channel)
    
    #Block until the terminal is closed, use ctrl-c to exit
    terminal.run()
 
   
