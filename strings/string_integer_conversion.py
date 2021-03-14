# String Integer Conversion pp71
# Time complexity O(n), Space Complexity O(n)
def string_int_conversion(a: str) -> int:
	power = 1
	sign = 1
	answer = 0
	for i in range(len(a)-1, -1, -1):
		if a[i] == '-' and i == 0:
			sign = -1
		elif a[i] == '+' and i == 0:
			sign = 1
		else:
			answer += int(a[i]) * power
			power *= 10
	return answer * sign

b = string_int_conversion("-123")
print(b)