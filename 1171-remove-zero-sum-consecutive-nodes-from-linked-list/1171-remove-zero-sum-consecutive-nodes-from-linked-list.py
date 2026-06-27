# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        mp={}
        s=0
        cur=dummy
        while cur:
            s+=cur.val
            mp[s]=cur
            cur=cur.next
        s=0
        cur=dummy
        while cur:
            s+=cur.val
            cur.next=mp[s].next
            cur=cur.next
        return dummy.next