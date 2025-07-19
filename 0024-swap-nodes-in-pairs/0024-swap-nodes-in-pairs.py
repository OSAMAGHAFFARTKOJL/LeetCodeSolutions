# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        prev = ListNode(0,head)
        cur = prev.next
        temp = cur.next
        head = temp
        while cur and temp:
            
            cur.next = temp.next
            
            temp.next = cur
            print(temp.next)
            prev.next = temp
            prev = cur
            cur = cur.next
            if cur:
                temp = cur.next
            else:
                return head
            
        return head