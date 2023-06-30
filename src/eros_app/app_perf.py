import click
import time

from eros import Eros

from rich.live import Live
from rich.table import Table

from dataclasses import dataclass
from typing import Dict,Tuple
from si_prefix import si_format


    
class ErosPerf():
    def __init__(self, eros):
        self.eros = eros
        

            
    def generate_table(self) -> Table:
        """Make a new table."""
        table = Table(title="Eros Performance",title_justify="left")
        table.add_column("Channel",justify="right",style="cyan")
        table.add_column("RX",justify="right")
        table.add_column("RX rate",justify="right",style="blue")
        table.add_column("TX",justify="right")
        table.add_column("TX rate",justify="right",style="blue")
        for ch_id,(rx_channel,tx_channel) in self.eros.analytics.items():
            table.add_row( f"{ch_id}",
                          f"{si_format(rx_channel.get_total(), precision=2):>6s}B",
                          f"{si_format(rx_channel.get_rate(), precision=2)}b/s",
                          f"{si_format(tx_channel.get_total(), precision=2)}B", 
                          f"{si_format(tx_channel.get_rate(), precision=2)}b/s",) # f"{channel.get_rx_rate()}", f"{channel.get_total_rx()}

        return table
     
    
    
@click.command()
@click.option('--channel', default=1, help='Channel to log')
@click.pass_context
def perf(ctx,channel):
    # Check if the context is properly set
    if not ctx.obj.get('eros'):
        click.echo("No Eros object found",err=True)
        return False
    eros = ctx.obj['eros']
    perf =  ErosPerf(eros)
    
    click.echo(click.style(f"Starting the perf", fg='green'))
        
    with Live(perf.generate_table(), refresh_per_second=4) as live:
        while True:
            time.sleep(0.2)
            live.update(perf.generate_table())

