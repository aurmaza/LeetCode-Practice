class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(0,head)
        prev = dummyHead
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next

            else:
                prev = head
                head = head.next
        return dummyHead.next
