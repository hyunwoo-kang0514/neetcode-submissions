# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # 다음 노드를 잊어버리지 않게 저장
            nxt = curr.next
            # 현재 노드의 포인터 변경
            curr.next = prev
            # prev를 현재 노드로 설정
            prev = curr
            # 다음 노드로 이동
            curr = nxt
        return prev


        