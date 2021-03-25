# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = cur_result = ListNode()

        while l1 or l2 or carry:
            cur_l1 = cur_l2 = 0

            if l1:
                cur_l1 = l1.val
                l1 = l1.next

            if l2:
                cur_l2 = l2.val
                l2 = l2.next

            carry, val = divmod(carry + cur_l1 + cur_l2, 10)

            cur_result.next = ListNode(val)
            cur_result = cur_result.next

        return head.next
