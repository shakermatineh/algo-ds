# 4 byte little-endian format
# x01 in binary is 00000001, each hx number is from 0 to 15 or 4 bit in binary
# little endian format means LSB is at smallest memory address. 
# leftmost position is smallest memory address
byte_sequence = b'\x01\x00' # in binary 00000000 00000001
integer_value = int.from_bytes(byte_sequence, byteorder='little')
print("1: ", integer_value) # output: 1

# big Endian format opposite. MSB is at smallest memory position
byte_sequence = b'\x00\x01' # in binary 00000001 00000000
print("2: ", int.from_bytes(byte_sequence, byteorder='big')) # integer equivalent = 1

# Split and convert each 4-byte sequence
byte_sequence = b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00' # byte_sequence[0:1] is b'\x01' 
integers = [int.from_bytes(byte_sequence[i:i + 4], byteorder='little') for i in range(0, len(byte_sequence), 4)]
print("3: ", integers)  # Output: [1, 2, 3, 4]

# binary to integer and hex
binary_number = '00010010'
integer_value = int(binary_number, 2)
hexadecimal_value = hex(integer_value)
print("4: ", integer_value, hexadecimal_value)

# hex to binary and integer
hex_number = '1A3'
integer_value = int(hex_number, 16) # 3*16^0 + 10*16^2 + 1*16^2
binary_value = bin(integer_value)
print("5: ", integer_value, binary_value)

decimal_number = 123
print("6: ", int.from_bytes(decimal_number.to_bytes(4, byteorder='little'), byteorder='little'))