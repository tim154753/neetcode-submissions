# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        front = head
        back = head.next.next
        while back is not None:
            if front == back:
                return True
            else:
                if back.next is None:
                    break
                front = front.next
                back = back.next.next
        return False
        