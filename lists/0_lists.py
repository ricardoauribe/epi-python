# List Class

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

# Search for a key

def search_list(L:ListNode, key: int) ->ListNode:
	while L and L.data != key:
		L = L.next
	# If key was nt present in the list, L will have become null
	return L
