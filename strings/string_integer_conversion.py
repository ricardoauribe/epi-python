# String Integer Conversion pp71
# Time complexity O(n) since we traverse the array once to read and once to reverse, 
# Space Complexity O(n) since we need the same space as in the original
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

#b = string_int_conversion("-123")
#print(b)

def int_to_string(x:int) -> str:
	is_negative = True if x < 0 else False
	x = abs(x)
	s = []

	while x != 0:
		units = x % 10
		# Append the char digit using ascii 0 as reference + the digit, ord give the ascii number of '0'
		s.append(chr(ord('0')+ units))
		x //= 10
	print(s)
	#Adds the negative sign back if needed
	ans = ('-' if is_negative else '') + ''.join(reversed(s))
	return ans

print(int_to_string(-3456))