# Bitwise AND

#1010
a = 10
#0100
b = 4

#0000
bitwise_and = a & b

#1110
bitwise_or = a | b

#1110  - Returns 1 if one of the bit is 1 and other is 0 else returns false
bitwise_xor = a ^ b

print("bitwise and")
print(bitwise_and)

print("bitwise or")
print(bitwise_or)

print("bitwise xor")
print(bitwise_xor)


# Shift 1010 -> 0101
shift_a = a >> 1
print("shift a 1 location right")
print(shift_a)

# Shift 1010 -> 0101
shift_a2 = a << 1
print("shift a 1 location left")
print(shift_a2)

# Not - Returns one’s compliement of the number.
# ~1010 = -(1010 + 1) = -(1011) = -11
not_a = ~a
print("not a")
print(not_a)