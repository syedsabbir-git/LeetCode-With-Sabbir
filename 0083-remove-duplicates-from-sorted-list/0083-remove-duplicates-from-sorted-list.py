# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sett= set()
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if curr.val in sett:
                prev.next = curr.next
            else:
                sett.add(curr.val)
                prev= curr
            curr = curr.next
        return dummy.next
