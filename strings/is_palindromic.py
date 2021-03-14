#Is Palindromic
#Time complexity O(n) -> Traverse everything once, Space Complexity O(1) No additional space needed

def is_palindromic(s: str) -> bool:
	#The all() function returns True if all items in an iterable are true, otherwise it returns False.
	#return all(s[i] == s[~i] for i in range(len(s)//2))
	for i in range(len(s)//2):
		if s[i] != s[len(s)-i-1]:
			return False
	return True


print(is_palindromic("aabaa"))
print(is_palindromic("aa"))
print(is_palindromic("aabaad"))

a = 0
b = ~a
print(b)