'''
https://leetcode.com/problems/add-two-numbers/'''

# Definition for singly-linked list.
"""Решение, которое принимает LeetCode"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
        
        @staticmethod
        def from_ln(ld: ListNode):
            l = []
            while ld.next is not None:
                l.append(ld.val)
                ld = ld.next
            l.append(ld.val)
            return l
        
        def to_ln(self, l: list):
            first, *rest = l
            ln = ListNode(first)
            if rest:
                ln.next = self.to_ln(rest)
            return ln

        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                l1_ = self.from_ln(l1)
                l2_ = self.from_ln(l2)
                ot = int("".join([str(i) for i in l1_[::-1]])) + int("".join([str(i) for i in l2_[::-1]]))
                res = [int(j) for j in list(str(ot))[::-1]]       
                return self.to_ln(res)



"""Если не заморачиваться с ListNode"""
def addTwoNumbers(l1: list[int], l2: list[int]) -> int:
        ot = int("".join([str(i) for i in l1[::-1]])) + int("".join([str(i) for i in l2[::-1]]))
        return [int(j) for j in list(str(ot))[::-1]]


l1, l2 = [2,4,3], [5,6,4]
print(l1[::-1])
print(l2[::-1])
print(addTwoNumbers(l1, l2))

sol = Solution()
l1_ = sol.to_ln(l1)
l2_ = sol.to_ln(l2)
res = sol.addTwoNumbers(l1_, l2_)
print(sol.from_ln(res))

