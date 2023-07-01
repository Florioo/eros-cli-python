import click
from eros_core import Eros, RequestResponse
from .decorators import eros_check
import time



@click.command("m-cli", help="Machine oriented Command Line Interface for the Eros")
@click.option('--channel', default=7, type=int, help='Channel to connect to')
@click.pass_context
@eros_check
def app_machine_cli(ctx, channel):

    eros = ctx.obj.get('eros')
    click.echo(click.style(f"Starting the machine cli on channel {channel}", fg='green'))
   
    # Create a new RequestResponse object
    resp = RequestResponse(eros, channel)

    # Send test commands
    while True:
        time.sleep(0.01)
        print('m-cli>', end="")
        cmd = input()
        response = resp.send(cmd)
        print(response)
