#!/usr/bin/env python
# Has Cycle pp 88
#Complexity: O(a) + O(b) where is the number of nodes to get to the cycle and b the number of nodes inside the cycle
# Space O(1), no additional space was required, just pointers

from ListNode import ListNode

def has_cycle(head:ListNode) -> [ListNode]:
  
  # This function completes a full cycle to determine it's lenght
  # when start is equal to end we now we finish where whe started
  def cycle_len(end):
    start = end
    step = 0
    while True:
      step += 1
      start = start.next
      if start is end:
        return step

  # Creating 2 points that will move at different speeds
  fast = head
  slow = head

  # While the fast one has a next node we will iterate
  while fast and fast.next:
    # Moving the fast one twice as fast
    slow = slow.next
    fast = fast.next.next

    #If they are the same we found a cycle
    if slow is fast:
      # Whe achieve the start of the cycle
      # Now we move back to head 
      cycle_len_advanced_iter = head
      for _ in range(cycle_len(slow)):
        # We determine how many nodes from start to the point where the cycle started
        cycle_len_advanced_iter = cycle_len_advanced_iter.next

      it = head
      # Both iterators advance at the same speed
      while it is not cycle_len_advanced_iter:
        it = it.next
        cycle_len_advanced_iter = cycle_len_advanced_iter.next
      return it # iter is the start of the cycle
  return None # No cycle


a = ListNode(11)
b = ListNode(3)
c = ListNode(5)
d= ListNode(7)
e = ListNode(2)
f = ListNode(66)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c

ans = has_cycle(a)
print(ans.data)

