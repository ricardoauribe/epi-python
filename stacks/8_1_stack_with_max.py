#!/usr/bin/env python
# Stack with Max API pp 100
#Complexity: O(n) where , space O(1), since no additional memory

from collections import namedtuple

class Stack:
	ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', 'element', 'max')

	def __init__(self) -> None:
		self._element_with_cached_max: List[Stack.ElementWithCachedMax] = []

	def empty(self) -> bool:
		return len(self._element_with_cached_max) == 0

	def max(self) -> int:
		return self._element_with_cached_max[-1].max

	def pop(self) -> int:
		return self._element_with_cached_max.pop().element

	def push(self, x: int) -> None:
		self._element_with_cached_max.append(
			self.ElementWithCachedMax(x,
				x if self.empty() else max(x, self.max())
				)
		)

