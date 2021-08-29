"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    temp = head
    ans = temp
    even = True

    while temp.next is not None:
        if even:
            ans = ans.next
            even = False
        else:
            even = True
        temp = temp.next
    return ans
