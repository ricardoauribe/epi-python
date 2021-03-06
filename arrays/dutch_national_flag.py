#Dutch national Flag pp41
#Complexity: O(n) since it covers the array once, space O(1), since no additional memory

def dutch_flag_partition(pivot_index: int, A: [int]) -> None:
	#Get value at selected index
	pivot = A[pivot_index]
	#Get pointers to 3 sections of the array smaller than pivot, equal and larger
	smaller = 0
	current = 0
	larger = len(A)
	while current < larger:
		#If current value is smaller than the pivot swap with the latest that's equal
		if A[current] < pivot:
			temp = A[smaller]
			A[smaller] = A[current]
			A[current] = temp
			current += 1
			smaller +=1
		#If current value is equal to the pivot do nothing and move equal pointer
		elif A[current] == pivot:
			current += 1
		#If current value is greater than the pivot move it to larger section and decrease in one the pointer
		else:
			larger -= 1
			temp = A[current]
			A[current] = A[larger]
			A[larger] = temp
	print(A)


A = [-3, 0, 8, 6, 9, 33, 17, 65, 23, 7]
print(A)
dutch_flag_partition(9, A)