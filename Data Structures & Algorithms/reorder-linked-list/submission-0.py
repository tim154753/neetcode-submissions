# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
O(1) space is the main constraint.
    - Update list as we go along, so that by the time we reach the end, the algorithm is done.
    - Basically, treat the current sublist 0:i as a whole list and update links iteratively as we encounter more nodes.

After hint 2 :(
    - find midpoint of list. Probably doable with slow and fast pointers. Have fast pointer move to fast.next.next, slow move to slow.next. When fast is None, we reached end of list. Then l should be at midpoint. 
        - O(n) time, O(1) space.
    - Reverse list starting at midpoint.
        - O(n) time, O(1) space
    - Change head.next to midpoint, midpoint.next to head.next, etc until we reach end of one of lists. 

'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        l = head
        r = head
        while r and r.next:
            l = l.next
            r = r.next.next

        #now l should be just before start of part of list that needs to be reversed

        midpoint = l.next
        l.next = None

        #reverse list beginning at l

        prev = None
        curr = midpoint
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #prev is head of reversed list
        l1 = head
        l2 = prev
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2
        return



