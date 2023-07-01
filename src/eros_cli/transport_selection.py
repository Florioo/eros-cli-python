from eros import Eros, ErosSerial,ErosUDP,ErosTCP,ErosZMQ
import time
import click

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
def attach_app(app):
    uart.add_command(app)
    tcp.add_command(app)
    udp.add_command(app)
    zmq.add_command(app)
    
from .app.app_log  import app_log
from .app.app_cli  import app_cli 
from .app.app_zmq  import app_zmq
from .app.app_perf import app_perf
from .app.app_machine_cli import app_machine_cli
from .app.app_dump import app_dump

attach_app(app_log)
attach_app(app_cli)
attach_app(app_zmq)
attach_app(app_perf)
attach_app(app_machine_cli)
attach_app(app_dump)
