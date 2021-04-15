#!/usr/bin/env python
# Reverse a single sublist pp 87
#Complexity: O(f) where f is the final node to search, wort case could be the last so O(n), since no additional memory

from ListNode import ListNode

def reverse_sublist(l: ListNode, start: int, end:int) -> [ListNode]:
	#We need to add a dummy head node in case you want to reverse from the first node
	head = ListNode(0,l)
	sublist_head = head

	#Get one node ahead the starting point 
	for _ in range(1, start):
		sublist_head = sublist_head.next

	# Now reverse the sub list
	# Initialize prev, curr and next
	prev = None
	curr = sublist_head.next
	next = curr
	# Keep memory of where the list need to be linked back
	sublist_start = curr

	# For n inclusive iterations reverse the pointers
	for _ in range(end + 1 - start):
		# Get next item to keep the pointer
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	
	# Link the start of the list to the las node reversed: prev
	sublist_head.next = prev
	# Link the begining of the reversed list to the next link to the last reversed: curr
	sublist_start.next = curr
	#Return head.next to ommit the dummy head added
	return head.next


a = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2)))))
#b= reverse_sublist(a,1,4)
b= reverse_sublist(a,2,4)
b.print_list()
