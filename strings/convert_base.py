# Convert base pp73
# Time Complexity O(n), Space Complexity O(n)
import functools
import string

def convert_base(num_as_string: str, b1: int, b2: int) ->str:
	def construct_from_base(num_as_int, base):
		print(num_as_int % base)
		# If the received number (base 10) is 0 then break else do an integer division by the base 
		# calling the construct from base function and concatenate the module result  
		# converted to a hex value
		return ('' if num_as_int == 0 else 
						construct_from_base(num_as_int // base, base)+
						string.hexdigits[num_as_int % base].upper())

	#Evaluate if received number is negative
	is_negative = num_as_string[0] == '-'
	print(num_as_string[is_negative:])

	# Reduce will save the accumulated value
	# functools.reduce(function, iterable[, initializer])
	# string.hexdigits will give the hexadecimal letters ‘0123456789abcdefABCDEF’.
	# function: lambda 
	# iterable: string without - sign
	# initializer: 0
	# this calculated the integer base 16 version of the number
	num_as_int = functools.reduce(
		lambda 
			x, c: x * b1 + string.hexdigits.index(c.lower()), 
			num_as_string[is_negative:], 
			0)
	print(num_as_int)
	# Return the proper sign + 0 or a recursive call to construct from base using the integer 
	# version of the received number
	return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))

print(convert_base("-615", 7, 13))