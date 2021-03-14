#Is Palindromic
#Time complexity O(n) -> Traverse everything once, Space Complexity O(1) No additional space needed

def is_palindromic(s: str) -> bool:
	return all(s[i] == s[~i] for i in range(len(s)//2))


print(is_palindromic("aabaa"))
print(is_palindromic("aa"))
print(is_palindromic("aabaad"))