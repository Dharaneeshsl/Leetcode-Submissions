# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val=val
#         self.next=next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0)
        d.next=head
        p=d
        while p.next and p.next.next:
            a=p.next
            b=a.next
            a.next=b.next
            b.next=a
            p.next=b
            p=a
        return d.next