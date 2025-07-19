# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #use case

        if head is None:
            return head
        length = 0 # store the length of the nodes
        cur = head #cur pointer to iterate
        while cur:
            cur = cur.next
            length +=1
        #use case
        if length<k:
            return head
        # Now lets try to find the both nodes location
        node_1 = head

        for i in range(k-1):
            node_1 = node_1.next

        node_2 = head

        for i in range(length - (k)):
            node_2 = node_2.next

        node_1.val,node_2.val = node_2.val,node_1.val
        return head





        

        