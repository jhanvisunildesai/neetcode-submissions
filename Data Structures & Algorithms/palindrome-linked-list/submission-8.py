# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        retval = True
        # count = 0
        # prev = None
        curr = head
        new_head = None

        while curr:
            new_head = ListNode(curr.val, new_head)
            curr = curr.next
            curr1 = head
            curr2 = new_head
        print(count)

        while curr1 is not None and curr2 is not None:
            if curr1.val != curr2.val:
                retval = False
                break
            curr1 = curr1.next
            curr2 = curr2.next
        return retval