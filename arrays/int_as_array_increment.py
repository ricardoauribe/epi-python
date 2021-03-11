#Array Increment pp45
#Complexity, time =O(n) we need to traverse the whole array, space O(1) no additional memory was needed

from typing import List

def plus_one(A: List[int])-> List[int]:
	# increase in 1 the last location (most right)
	A[len(A)-1] += 1
	# start from the last location to 1
	for i in reversed(range(1, len(A))):
		#If the sum makes location value = 10, set it to 0 and carry on to next location
		if A[i] == 10:
			A[i] = 0
			A[i-1] += 1
	#For the first location if there is a carry on we append a 0 at the end for the extra digit needed
	#Since all but first location will be zeros it doesn't matter we attach it at the end
	if A[0] == 10:
		A[0] = 1
		A.append(0)
	return A


A =[9,9,9]
print(A)
B = plus_one(A) 
print(B)
