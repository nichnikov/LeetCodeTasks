'''
https://leetcode.com/problems/add-two-numbers/'''

"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ot = int("".join(sorted(l1, revers=True))) + int("".join(sorted(l2, revers=True)))
        return sorted(list(ot), revers=True)
"""

def addTwoNumbers(l1: list[int], l2: list[int]) -> int:
        ot = int("".join([str(i) for i in l1[::-1]])) + int("".join([str(i) for i in l2[::-1]]))
        return list(str(ot))[::-1]

l1, l2 = [2,4,3], [5,6,4]
print(l1[::-1])
print(l2[::-1])
print(addTwoNumbers(l1, l2))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

t1 = ListNode(3)
print("t1.val:", t1.val)

from typing import Optional

class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ot = int("".join([str(i) for i in l1[::-1]])) + int("".join([str(i) for i in l2[::-1]]))
        return list(str(ot))[::-1]

s = Solution.addTwoNumbers(l1, l2)
print(s)