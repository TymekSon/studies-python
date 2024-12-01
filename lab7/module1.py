filepath = "iris.txt"
f = open(filepath)

lines = f.readlines()
# print(lines)

f.close()

import struct

number = 4567
number_c = struct.pack('i', number)
print(number_c)