#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        vals = set()
        curr = dummyHead = ListNode(0, head)
      
        while curr and curr.next:
            if curr.next.val in vals:
                curr.next = curr.next.next 
            else:
                vals.add(curr.next.val)
                curr = curr.next
        return dummyHead.next
                
                
                
                