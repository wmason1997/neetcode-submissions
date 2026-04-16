# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        array = []
        #array.append(cur)

        while cur:
            array.append(cur)
            cur = cur.next
        
        removeIndex = len(array) - n
        if removeIndex == 0:
            return head.next
        array[removeIndex - 1].next = array[removeIndex].next

        return head
