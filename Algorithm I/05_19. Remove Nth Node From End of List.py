"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    temp = head
    node_to_del = head
    pointer = n
    count_nodes = 1

    while temp.next is not None:
        if pointer == 0:
            node_to_del = node_to_del.next
        else:
            pointer -= 1
        temp = temp.next
        count_nodes += 1
    if head.next is None:
        head = None
    elif node_to_del == head and count_nodes == n:
        head = head.next
    else:
        node_to_del.next = node_to_del.next.next
    return head
