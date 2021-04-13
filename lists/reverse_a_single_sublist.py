#!/usr/bin/env python
# Reverse a single sublist pp 87
#Complexity: O(n + m) where m + n are the lenghts of the 2 lists, space O(1), since no additional memory

from ListNode import ListNode

def reverse_sublist(l: ListNode, start: int, end:int) -> [ListNode]:
	head = l
	sublist_head = head

	#Get to the starting point one node ahead
	for _ in range(1, start-1):
		sublist_head = sublist_head.next

	# Now reverse the list
	# Get the first item to reverse
	sublist_items = sublist_head.next
	# For n inclusive iterations
	for _ in range(end - start):
		# Get next item to keep the pointer
		temp = sublist_items.next
		
		sublist_items.next = temp.next
		temp.next = sublist_head.next
		sublist_head.next = temp
	
	return head


a = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2)))))
b= reverse_sublist(a,2,4)
b.print_list()
