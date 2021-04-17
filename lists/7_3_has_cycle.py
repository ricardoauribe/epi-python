#!/usr/bin/env python
# Has Cycle pp 88
#Complexity: O(a) + O(b) where is the number of nodes to get to the cycle and b the number of nodes inside the cycle
# Space O(1), no additional space was required, just pointers

from ListNode import ListNode

def has_cycle(head:ListNode) -> [ListNode]:
  def cycle_len(end):
    start = end
    step = 0
    while True:
      step += 1
      start = start.next
      if start is end:
        return step

  fast = head
  slow = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow is fast:
      # Whe achieve the start of the cycle
      cycle_len_advanced_iter = head
      for _ in range(cycle_len(slow)):
        cycle_len_advanced_iter =cycle_len_advanced_iter.next

      it = head
      # Both iterators advance in tandem
      while it is not cycle_len_advanced_iter:
        it = it.next
        cycle_len_advanced_iter = cycle_len_advanced_iter.next
      return it # iter is the start of the cycle
  return None # No cycle


com = ListNode(66)
#com.print_list()
a = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2, com)))))
com.next = a
ans = has_cycle(a)
print(ans.data)

