# Convert base pp73
# Time Complexity O(n), Space Complexity O(n)
import functools
import string

def convert_base(num_as_string: str, b1: int, b2: int) ->str:
	def construct_from_base(num_as_int, base):
		# If the received number is 0 then break else do an integer division by the base 
		# calling the construct from base function and concatenate the module result  
		# converted to a hex value
		return ('' if num_as_int == 0 else 
						construct_from_base(num_as_int // base, base)+
						string.hexdigits[num_as_int % base].upper())
	
	is_negative = num_as_string[0] == '-'
	# Reduce will save the accumulated value
	num_as_int = functools.reduce(lambda x, c: x * b1 + string.hexdigits.index(c.lower()), num_as_string[is_negative:], 0)
	return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))

print(convert_base("615", 7, 13))