from eros import Eros 
from blessed import Terminal
import threading
import time
from queue import Queue
class ErosTerminal():
    def __init__(self, eros:Eros, main_channel, aux_channel) -> None:
        self.eros = eros
        self.main_channel = main_channel
        self.aux_channel = aux_channel

        self.main_receive_buffer = b""
        self.main_transmit_queue = Queue()
                
        self.eros.attach_channel_callback(self.main_channel, self.receive_main)
        self.eros.attach_channel_callback(self.aux_channel, self.receive_aux)
       
        self.transmit_thread_handle = threading.Thread(target=self.transmit_thread, daemon=True)
        
    def transmit_thread(self):
        last_transmit = time.time()
        while True:
            buffer = bytearray()
            
            # If we are repeatedlt transmitting, wait a bit
            if time.time() - last_transmit < 0.025:
                time.sleep(0.025)
            
            while True:
                buffer += self.main_transmit_queue.get()
                if self.main_transmit_queue.empty():
                    break
            
            last_transmit = time.time()
            self.eros.transmit_packet(self.main_channel, bytes(buffer))
        
    def receive_main(self, data):
        first_byte = data[0]
        
        if not first_byte:
            self.main_receive_buffer += data[1:]
            return
            
        first_byte -=1 
        
        is_error = first_byte >0
        
        if is_error:
            # Colorize
            if len(self.main_receive_buffer) > 0:
                self.terminal_write(f"\033[91mError: {self.main_receive_buffer.decode()}\033[0m\n")
            else:
                self.terminal_write(f"\033[91mError\033[0m\n")
        else:
            if len(self.main_receive_buffer) > 0:        
                self.terminal_write(f"{self.main_receive_buffer.decode()}\n")
            else:
                self.terminal_write(f"\033[92mOK\033[0m\n")
        self.main_receive_buffer = b""    
        
    def receive_aux(self, data):
        self.terminal_write(f"{data.decode()}")
        
    def terminal_write(self, text):
        print(text, end="")
        
        # Smehow this is needed to make the terminal work
        with self.terminal.location(x=0, y=0):
            pass
            
                    
    def run(self):
        self.transmit_thread_handle.start()
        self.terminal = Terminal()

        print( self.terminal.clear)
        self.eros.transmit_packet(self.main_channel, "\n")
         
        with self.terminal.location(x=0, y=0):
            print(self.terminal.black_on_darkkhaki(self.terminal.center('EROS Terminal')))
                    
        with self.terminal.cbreak(): #), self.terminal.hidden_cursor()
            while True:

                # Read a character from the terminal
                inp = self.terminal.inkey()         
                #Send the character to the main channel     
                # self.main_transmit_buffer += inp.encode()  
                self.main_transmit_queue.put(inp.encode())
  
