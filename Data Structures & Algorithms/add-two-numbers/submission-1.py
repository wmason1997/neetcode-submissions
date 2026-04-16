class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1, str2 = '', ''
        l1_cur = l1
        l2_cur = l2

        # Get strings
        while l1_cur:
            str1 += str(l1_cur.val)
            l1_cur = l1_cur.next

        while l2_cur:
            str2 += str(l2_cur.val)
            l2_cur = l2_cur.next
        
        # Reverse strings
        str1 = str1[::-1]
        str2 = str2[::-1]

        # Cast to ints and add
        total = int(str1) + int(str2)

        # Cast to string
        total = str(total)
        total = total[::-1]

        # build out a new linked list
        dummy = ListNode(0)
        curr = dummy

        for s in total:
            curr.next = ListNode(int(s))
            curr = curr.next

        # Return head
        return dummy.next