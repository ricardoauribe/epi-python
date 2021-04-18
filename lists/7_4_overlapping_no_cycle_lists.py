#!/usr/bin/env python
# Overlapping Lists with no cycle pp 90
#Complexity: O(a) + O(b) where is the number of nodes to get to the cycle and b the number of nodes inside the cycle
# Space O(1), no additional space was required, just pointers

from ListNode import ListNode

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
  print("something")


a = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2)))))
b = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2)))))

overlapping_no_cycle_lists(a, b)