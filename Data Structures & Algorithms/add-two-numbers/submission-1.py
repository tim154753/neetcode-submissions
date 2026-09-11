# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Idea:
    - Digits are stored in reverse order. So 321 = 1->2->3, 7654 = 4->5->6->7.
    - This is actually nice, because it means digits are already aligned. So, we should just be able to keep a carry and rem term and pass it through until we reach the end of one or both lists. If we reach the end of one list, treat each next term as a 0 and proceed with any left over carrying that needs to be done. If a carry term is left over when we reach the end of both lists, make tail.next link to node with value 1.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        carry = 0
        prev = l1
        while (node1.val + node2.val + carry) != 0:
            res = node1.val + node2.val + carry
            node1.val = res % 10
            carry = res // 10
            if not node1.next:
                node1.next = ListNode()
            if not node2.next:
                node2.next = ListNode()
            prev = node1
            node1 = node1.next
            node2 = node2.next
        prev.next = None
        return l1
            
            