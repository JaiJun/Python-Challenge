"""
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Input: head = [1,2]
    Output: [2,1]
    Example 3:

    Input: head = []
    Output: []
"""
def reverseList(head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head
if __name__ == '__main__':
    head = [1, 2]
    reverseList(head)