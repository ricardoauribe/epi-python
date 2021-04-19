#!/usr/bin/env python
# Overlapping Lists with no cycle pp 90
# Complexity: O(n)
# Space O(1), no additional space was required, just pointers

from ListNode import ListNode

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
  def length(l: ListNode):
    length = 0
    while l:
      length += 1
      l = l.next
    return length

  l0_len = length(l0)
  l1_len = length(l1)

  if l0_len > l1_len:
    # make it so l1 is the longer list
    l0p = l1
    l1p = l0
  else:
    l0p = l0
    l1p = l1

  print(l0p.data)
  print(l1p.data)

  # We advance the longer list to get the equal length lists
  for _ in range(abs(l0_len - l1_len)):
    l1p = l1p.next

  while l0p and l1p and l0p is not l1p:
    l0p = l0p.next
    l1p = l1p.next
  # If we get to the last one and get to None it implies there was no overlap
  return l0p


overlap = ListNode(43, ListNode(8, ListNode(9)))

a = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2, overlap)))))
b = ListNode(15, ListNode(34, ListNode(54, overlap)))

ans = overlapping_no_cycle_lists(a, b)
print(ans.data)