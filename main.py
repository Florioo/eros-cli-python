from eros import Eros, ErosSerial,ErosUDP,ErosTCP
import time
import click


def start_eros_log(transport, channel):
    eros = Eros(transport)
    eros.attach_channel_callback(channel, lambda data: print(data.decode(),end=""))
    eros.spin()

@click.group()
def eros_log():
    pass


@eros_log.command()
@click.argument('channel', type=int, default=1)
@click.option('--port', default="auto", help='Port to use for UART communication')
@click.option('--baud', default=2000000, help='Baud rate for UART communication')
@click.option('--vid', default=4292, help='Vendor ID automatic serial port detection')
def uart(channel, port, baud, vid):
    click.echo(click.style(f"Opening UART channel on {channel} with port '{port}' and baud {baud}", fg='green'))
    
    try:
        transport = ErosSerial(port=port, baudrate=baud,vid=4292)
    except Exception as e:
        click.echo(click.style(f"Failed to open UART: {e}", fg='red'))
        return
    
    start_eros_log(transport, channel)

        
@eros_log.command()
@click.argument('channel', type=int)
@click.option('--ip', default='192.168.0.1', help='IP address to use for UDP communication')
@click.option('--port', default=5555, help='Port to use for UDP communication')
def udp(channel, ip, port):
    click.echo(f"Running UDP channel {channel} with IP {ip} and port {port}")
    start_eros_log(ErosUDP(ip, port),channel)
    
@eros_log.command()
@click.argument('channel', type=int)
@click.option('--ip', default='192.168.0.1', help='IP address to use for TCP communication')
@click.option('--port', default=6666, help='Port to use for TCP communication')
def tcp(channel, ip, port):
    click.echo(f"Running TCP channel {channel} with IP {ip} and port {port}")
    start_eros_log(ErosTCP(ip, port),channel)

if __name__ == '__main__':
    eros_log()