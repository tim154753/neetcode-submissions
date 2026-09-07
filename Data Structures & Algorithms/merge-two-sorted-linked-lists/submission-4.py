# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Idea:
    - Start at head of list1. Compare to head of list2. 
        - If head1 > head 2, set temp = head2.next, set head2.next = head1. 
        - If head1 <= head2, set temp = head1.next, head1.next = head2.
    - Now, the heads are sorted. What to do with their original next elements?
    - 
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            curr1 = list1
            curr2 = list2
        else:
            curr1 = list2
            curr2 = list1
        head = curr1
        while curr2 is not None:
            while curr1.next is not None and curr1.next.val <= curr2.val:
                curr1 = curr1.next
            temp = curr1.next
            curr1.next = curr2
            curr2 = temp
        return head
        