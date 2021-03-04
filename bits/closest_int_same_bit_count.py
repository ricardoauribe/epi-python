# Closest number with same weight
print("Closest number with same weight")
# 7 = 0111
def closest_int_same_bit_count(x: int) -> int:
	num_unsigned_bits = 64
	print("x in binary")
	print("{0:b}".format(x))
	for i in range(num_unsigned_bits -1):
		# iterate until bits at i and i +1 are different starting from the LSB
		if (x >> i) & 1 != (x >> (i+1)) & 1:
			#bits are different so they can be swaped
			print("bit at i where i and i+1 are different")
			print("{0:b}".format(1 << i))
			print("bit at i +1")
			print("{0:b}".format(1 << (i+1)))
			print("or between i and i+1")
			print("{0:b}".format(1 << i | 1 << (i+1)))
			print("xor with x")
			print("{0:b}".format(x ^ 1 << i | 1 << (i+1)))
			x ^= (1 << i) | (1 << (i +1)) # swaps bits - i and bits - i+1
			return x

ans = closest_int_same_bit_count(7)
print(ans)
