# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        dummy.next = head
        first = head
        second = dummy
        k = n

        while k>0:
            first = first.next
            k -= 1
        while first:
            second = second.next
            first = first.next
        
        second.next = second.next.next

        return dummy.next
