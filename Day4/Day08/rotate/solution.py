#!/usr/bin/python

import sys
import math
import struct

u = lambda x: struct.unpack('f', x)[0]
p = lambda x: struct.pack('b', x)

if len(sys.argv) != 3:
	sys.exit(1)

filename = sys.argv[1]
key = math.radians(int(sys.argv[2]))

print key

bs = open(filename, 'rb').read()
dec = open(filename[0:-8] + "_decoded" + sys.argv[2] + ".jpg", 'wb')

for i in range(0,len(bs),8):
	x, y = u(bs[i:i+4]), u(bs[i+4:i+8])
	# F**K YOU PYTHON, YOU STUPID TRUNCATION, LEARN HOW TO ROUND YOU DING DONG
	dec.write(p(round(x * math.cos(key) + y * math.sin(key), 0)) + p(round(y * math.cos(key) - x * math.sin(key), 0)))
