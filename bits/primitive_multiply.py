# Multiply
print("Multiply")

def multiply(x: int, y:int) -> int:
	def add(a,b):
		return a if b == 0 else add(a ^ b, (a & b) << 1)

	running_sum = 0
	while x:
		if x & 1:
			running_sum = add(running_sum, y)
		x, y = x >> 1, y << 1
	return  running_sum

ans2 = multiply(3,9)
print(ans2)