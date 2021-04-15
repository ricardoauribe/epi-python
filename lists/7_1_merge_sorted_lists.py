#!/usr/bin/env python
#Merge 2 sorted lists pp 86
#Complexity: O(n + m) where m + n are the lenghts of the 2 lists, space O(1), since no additional memory

from ListNode import ListNode

def merge_two_sorted_lists(l1: [ListNode], l2: [ListNode]) ->[ListNode]:
	# Creates a placeholder for the result
	head = ListNode()
	tail = head
	# Start building tail with the smaller value and move pointer of the list where it got used
	while l1 and l2:
		if l1.data <= l2.data:
			tail.next = l1
			l1 = l1.next
		else:
			tail.next = l2
			l2 = l2.next
		# move tail to the actual node that was smaller
		tail = tail.next
	
	# Append the remaining nodes
	tail.next = l1 or l2
	return head.next

a = ListNode(2, ListNode(5, ListNode(7)))
b = ListNode(3, ListNode(11))
a.print_list()
b.print_list()

print("Merge and Sorted:")
c = merge_two_sorted_lists(a,b)
c.print_list()