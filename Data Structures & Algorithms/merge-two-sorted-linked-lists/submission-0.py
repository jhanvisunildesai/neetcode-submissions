# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        retval = ListNode()
        curr = retval
        list1curr = list1
        list2curr = list2
        while list1curr != None and list2curr != None:
            if(list1curr.val > list2curr.val):
                curr.next = ListNode(list2curr.val)
                list2curr = list2curr.next
            else:
                if(list1curr.val < list2curr.val):
                    curr.next = ListNode(list1curr.val)
                    list1curr = list1curr.next
                else:
                    if(list1curr.val == list2curr.val):
                        curr.next = ListNode(list2curr.val)
                        list2curr = list2curr.next
                        curr = curr.next
                        curr.next = ListNode(list1curr.val)
                        list1curr = list1curr.next
            curr = curr.next
            # print(retval.val)
        if list1curr != None or list2curr != None:
            while list2curr != None:
                curr.next = ListNode(list2curr.val)
                list2curr = list2curr.next
                curr = curr.next
            while list1curr != None:
                curr.next = ListNode(list1curr.val)
                list1curr = list1curr.next
                curr = curr.next
                
        return retval.next
        