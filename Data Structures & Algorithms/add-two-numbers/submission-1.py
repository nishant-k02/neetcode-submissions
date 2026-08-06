# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        currentNode = dummyNode
        temp1 = l1
        temp2 = l2
        carry = 0

        while temp1 or temp2:
            sums = carry
            if temp1:
                sums += temp1.val 
            if temp2:
                sums += temp2.val     
            carry = sums // 10
            sums = sums % 10
            newNode = ListNode(sums)
            currentNode.next = newNode
            currentNode = currentNode.next

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        
        if carry:
            newNode = ListNode(carry)
            currentNode.next = newNode
        return dummyNode.next

        