# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        prev_group = dummy
        while True:
            kth = self.get_kth_node(prev_group,k)
            if not kth:
                break
            
            group_next = kth.next
            prev = group_next
            cur = prev_group.next

            while cur != group_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
        return dummy.next


    def get_kth_node(self,head,k):
        while head and k>0:
            head = head.next 
            k -=1
        return head
            

 

