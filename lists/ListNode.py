#!/usr/bin/env python
# List Class

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

	def print_list(self):
		while self:
			print(self.data)
			self = self.next
