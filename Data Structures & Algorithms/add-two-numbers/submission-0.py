class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        arr1 = []
        arr2 = []

        while l1:
            arr1.append(l1.val)
            l1 = l1.next

        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        arr1.reverse()
        arr2.reverse()

        str1 = ""
        for num in arr1:
            str1 += str(num)

        num1 = int(str1)

        str2 = ""
        for num in arr2:
            str2 += str(num)

        num2 = int(str2)

        res = str(num1 + num2)

        dummy = ListNode()
        current = dummy

        for ch in reversed(res):
            current.next = ListNode(int(ch))
            current = current.next

        return dummy.next