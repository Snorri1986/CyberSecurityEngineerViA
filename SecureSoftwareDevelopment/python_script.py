import struct
from capstone import *

x = b"computer"

print(f"# Data withOut meaning:")
print(f"    {' '.join(format(x, '02x') for x in x)}")
print(f"    {x.hex()}")


print("# Data with meaning:")
print("    8 8-bit integers:          ", struct.unpack("BBBBBBBB", x))
print("    4 unsigned 16-bit integers:", struct.unpack("HHHH", x))
print("    2 unsigned 32-bit integers:", struct.unpack("II", x))
print("    1 unsigned 64-bit integer: ", struct.unpack("Q", x))
print("    a 64-bit pointer:          ", hex(struct.unpack("P", x)[0]))
print("    2 32-bit floats:           ", struct.unpack("ff", x))
print("    1 64-bit float:            ", struct.unpack("d", x))
print("    2 RGB colors:              ", struct.unpack("BBBBBBBB", x))

print("ASM 64 isntructions:")
md = Cs(CS_ARCH_X86, CS_MODE_64)
for i in md.disasm(x, 0x0):
    print(" 0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))

print("ASM 32 isntructions:")
md = Cs(CS_ARCH_X86, CS_MODE_32)
for i in md.disasm(x, 0x0):
    print(" 0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))


print("ARM isntructions:")
md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
for i in md.disasm(x, 0x0):
    print(" 0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))