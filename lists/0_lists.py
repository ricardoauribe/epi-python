# List Class

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

# Search for a key, O(n)

def search_list(L:ListNode, key: int) ->ListNode:
	while L and L.data != key:
		L = L.next
	# If key was nt present in the list, L will have become null
	return L

# Insert new node after node O(1)

def insert_after(node: ListNode, new_node: ListNode) ->None:
	new_node.next = node.next
	node.next = new_node

# Delete a node past this one. Assume node is not a tail O(1)

def delete_after(node: ListNode) -> None:
	node.next = node.next.next