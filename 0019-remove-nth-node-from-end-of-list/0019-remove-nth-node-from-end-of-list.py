# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ct=0
        temp=head
        while temp is not None:
            ct+=1
            temp=temp.next
        if ct==n:
            return head.next
        prev=head
        for _ in range(ct-n-1):
            prev=prev.next
        prev.next=prev.next.next
        return head
        