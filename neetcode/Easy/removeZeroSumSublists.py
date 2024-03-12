# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        curr = dummyHead
        prefixSum = 0
        prefixSumToNode = {}
        while curr:
            prefixSum += curr.val
            prefixSumToNode[prefixSum] = curr
            curr = curr.next
        prefixSum = 0
        curr = dummyHead
        while curr:
            prefixSum += curr.val
            curr.next = prefixSumToNode[prefixSum].next
            curr = curr.next
        return dummyHead.next
