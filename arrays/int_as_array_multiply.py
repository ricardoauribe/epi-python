#Multiply 2 integer represented by arrays pp46
#time complexity O(n) Space Complexity O(1)
from typing import List

def multiply(num1: List[int], num2: List[int]) ->List[int]:
	print(A)
	print(B)
	# Get the sign for the resulting operation
	if(num1[0]<0) ^ (num2[0]<0):
		sign = -1
	else:
		sign = 1
	#make both numbers positive
	num1[0] = abs(num1[0])
	num2[0] = abs(num2[0])

	#resulting number size will be of num1 lenght + num2 lenght
	result = [0] * (len(num1) + len(num2))
	print(result)
	#Range goes from 0 to num len - 1
	for i in reversed(range(len(num1))):
		for j in reversed(range(len(num2))):
			#Get digit multiplication and add it to existing previous sum
			result[i+j+1] += num1[i] * num2[j]
			#this will keep the tens, integer division
			result[i+j] += result[i+j+1] // 10
			#This will keep the units
			result[i+j+1] %=10
	
	#Remove extra 0's
	idx=0
	while result[idx] == 0:
		del result[idx]

	#Apply sign
	result[0] *= sign
	return result

A = [-1,1,1]
B = [9,8,9,3]
C = multiply(A,B)
print(C)

