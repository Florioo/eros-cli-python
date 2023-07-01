from eros import Eros, ErosSerial,ErosUDP,ErosTCP,ErosZMQ
import time
import click
from .app_log import log as app_log
from .app_cli import cli as app_cli 
from .app_zmq import zmq as app_zmq
from .app_perf import perf as app_perf
from .app_test import test as app_test

@click.group(chain=True)
@click.option('--port', default="auto", help='Port to use for UART communication')
@click.option('--baud', default=2000000, help='Baud rate for UART communication')
@click.option('--vid', default=4292, help='Vendor ID automatic serial port detection')
@click.pass_context
def uart(ctx,port, baud, vid):
    click.echo(click.style(f"Opening UART with port '{port}' and baud {baud}", fg='green'))
    ctx.ensure_object(dict)
    
    try:
        transport = ErosSerial(port=port, baudrate=baud,vid=4292)
        ctx.obj['eros'] = Eros(transport)
    
    except Exception as e:
        click.echo(click.style(f"Failed to open UART: {e}", fg='red'))

@click.group(chain=True)
@click.option('--ip', default='192.168.0.1', help='IP address to use for UDP communication')
@click.option('--port', default=5555, help='Port to use for UDP communication')
@click.pass_context
def udp(ctx,ip, port):
    click.echo(f"Opening UDP with IP {ip} and port {port}")
    ctx.ensure_object(dict)

    transport = ErosUDP(ip, port)
    ctx.obj['eros'] = Eros(transport)
    
@click.group(chain=True)
@click.option('--ip', default='192.168.0.1', help='IP address to use for TCP communication')
@click.option('--port', default=6666, help='Port to use for TCP communication')
@click.pass_context
def tcp(ctx, ip, port):
    click.echo(f"Opening TCP with IP {ip} and port {port}")
    ctx.ensure_object(dict)
    transport = ErosTCP(ip, port)
    ctx.obj['eros'] = Eros(transport)
    
@click.group(chain=True)
@click.option('--port', default=2000, help='Port to use for ZMQ communication')
@click.pass_context
def zmq(ctx, port):
    click.echo(f"Opening ZMQ with port {port}")
    ctx.ensure_object(dict)
    transport = ErosZMQ( port)
    ctx.obj['eros'] = Eros(transport)


@uart.result_callback()
@zmq.result_callback()
@tcp.result_callback()
@udp.result_callback()
def process_pipeline(data,**kwargs):
    for ret in data:
        if ret == False:
            return
    click.echo(click.style(f"Waiting for applicaiton to finish", fg='white'))
        
    while True:
        time.sleep(1)
        
# Register the log command with the transport groups
uart.add_command(app_log)
tcp.add_command(app_log)
udp.add_command(app_log)
zmq.add_command(app_log)

uart.add_command(app_cli)
tcp.add_command(app_cli)
udp.add_command(app_cli)
zmq.add_command(app_cli)

uart.add_command(app_zmq)
tcp.add_command(app_zmq)
udp.add_command(app_zmq)
zmq.add_command(app_zmq)

uart.add_command(app_perf)
tcp.add_command(app_perf)
udp.add_command(app_perf)
zmq.add_command(app_perf)


uart.add_command(app_test)
tcp.add_command(app_test)
udp.add_command(app_test)
zmq.add_command(app_test)
