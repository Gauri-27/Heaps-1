# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time complexity: O(Nlogk)
# Space Complexity : O(N)

from heapq import heappop, heappush
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heappush(heap,(node.val, i, node))
        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = node
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        
        