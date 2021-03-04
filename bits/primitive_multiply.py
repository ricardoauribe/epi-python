# Multiply
print("Multiply")

def multiply(x: int, y:int) -> int:

	print(x, " x = ", "{0:b}".format(x))
	print(y, " y = ", "{0:b}".format(y))

	def add(a,b):
		print("{0:b}".format(a))
		print("{0:b}".format(b))
		# If there is nothing to add return the number
		# Else return the sum of a + b with the xor operation + the carry over with the and operation shifted by 1 location
		return a if b == 0 else add(a ^ b, (a & b) << 1)

	running_sum = 0
	while x:
		print("number ", x, " x = ", "{0:b}".format(x))
		if x & 1:
			print("bit is 1 so will add it")
			running_sum = add(running_sum, y)
			print("running_sum: ", "{0:b}".format(running_sum))
		# this is a double assignation x = x>> 1, y = y<<1
		# once we got a bit processed we shift x to process the next bit and shift y to the right to reflect the new number
		x, y = x >> 1, y << 1
		print(x, " x = ", "{0:b}".format(x))
		print(y, " y = ", "{0:b}".format(y))
	return  running_sum

ans2 = multiply(7,9)
print(ans2)