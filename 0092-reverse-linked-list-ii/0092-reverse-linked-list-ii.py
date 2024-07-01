# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
            
        temp_head = ListNode(0)
        temp_head.next = head
        prev = temp_head
                
        for i in range(left - 1):
            prev = prev.next
                
        current = prev.next
                
        for i in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
                
        return temp_head.next
        