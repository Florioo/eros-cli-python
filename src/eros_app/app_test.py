import click
import time

from eros import Eros
import threading

def print_test():
    while True:
        click.echo("Hello World")
        time.sleep(1)
        
        
@click.command()
@click.option('--channel', default=1, help='Channel to log')
@click.pass_context
def test(ctx,channel):
    # Check if the context is properly set
    if not ctx.obj.get('eros'):
        click.echo("No Eros object found",err=True)
        return False

    
    eros = ctx.obj['eros']

    # perf =  ErosPerf(eros)
    # Create the thread
    thread = threading.Thread(target=print_test,daemon=True)
    thread.start()

