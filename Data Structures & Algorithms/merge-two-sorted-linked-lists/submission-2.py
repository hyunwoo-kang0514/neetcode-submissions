class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next

            elif list1.val == list2.val:
                node1 = list1
                node2 = list2

                list1 = list1.next
                list2 = list2.next

                dummy.next = node1
                dummy = dummy.next

                dummy.next = node2
                dummy = dummy.next

            else:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next

        while list1:
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next

        while list2:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next

        return head.next