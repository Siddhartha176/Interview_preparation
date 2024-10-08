# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = result = ListNode(next)     #Dumy Head
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            pre.next = ListNode(carry % 10)
            pre = pre.next
            carry //= 10
            
        return result.next
""""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

l1 = [2,4,3]
l2 = [5,6,4]
Solution
addTwoNumbers(l1,l2)"""