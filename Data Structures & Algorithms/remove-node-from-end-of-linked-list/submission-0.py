# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = head
        temp = head
        # size of the list
        size = 0
        # get the size of the list
        current = head
        while current:
            current = current.next
            size += 1

        if n == size:
            return head.next
        
        i = 1
        beforeN = size - n
        while i < beforeN:
            temp = temp.next
            i += 1

        temp.next = temp.next.next

        return res




        
            

        