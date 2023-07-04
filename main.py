# Create a bridge between a TCP socket and a serial port
import socket, select, string, sys
import serial

host = "telehack.com"
port = 23
serial_port = "COM12"

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.settimeout(2)
#s.connect((host, port))

state = 0
line_accumulator = bytearray()

ser = serial.Serial(serial_port, 9600, timeout=1)

def process_line(line):
    if line[0] == 26 and line[1] == 26:
        print("Line: ", line_accumulator.decode())

while True:

    # Accumulate lines in case there are commands that we should be acting on
    if ser.in_waiting:
        r = ser.read(1)
        if r[0] == 10:
            process_line(line_accumulator)            
            line_accumulator.clear()
        else:
            line_accumulator.append(r[0])
    """
    if state == 0:
    elif state == 1:

        if s:
            # Check for inbound data
            socket_list = [ s ]
            read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [], 0 ) 
            for sock in read_sockets:
                msg = sock.recv(1024)
                print(msg.decode("ascii", errors="ignore"))
                sys.stdout.write(msg.decode("ascii", errors="ignore"))
                sys.stdout.flush()
    """
