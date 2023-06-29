from eros import Eros, ErosSerial,ErosUDP,ErosTCP
import time
import click
import app_log
import app_terminal
    
@click.group()
def cli():
    pass

cli.add_command(app_log.log)
cli.add_command(app_terminal.cli)

if __name__ == '__main__':
    cli()