# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                l1_value = l1.val 
            else:
                l1_value = 0

            if l2:
                l2_value = l2.val
            else:
                l2_value = 0

            result = l1_value + l2_value + carry 
            current.next = ListNode(result % 10)
            carry = result // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current = current.next

        return dummy.next