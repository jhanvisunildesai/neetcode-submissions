# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        retval = False
        temp = []
        curr = head
        while curr!= None:
            if curr not in temp:
                temp.append(curr)
            else:
                retval = True
                break
            curr = curr.next
        print(temp)
        return retval
        