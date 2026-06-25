# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(curr, k):
            while curr and k:
                curr = curr.next
                k -= 1
            return curr

        def reverse(start, end):
            prev = end
            while start != end:
                nxt = start.next
                start.next = prev
                prev = start
                start = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            start = groupPrev.next
            newHead = reverse(start, groupNext)
            groupPrev.next = newHead
            groupPrev = start

        return dummy.next