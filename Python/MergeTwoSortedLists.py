# -*- coding: UTF-8 -*-
#
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
# Python, Python 3 all accepted.
class MergeTwoSortedLists:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        fakeHeader = result

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                result.next = ListNode(l2.val)
                l2 = l2.next
            result = result.next

        if l1 is None:
            result.next = l2
        else:
            result.next = l1

        return fakeHeader.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "ListNode val: " + str(self.val) + " next: -> " + str(self.next)


m = MergeTwoSortedLists()

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(4)

n2 = ListNode(1)
n2.next = ListNode(3)
n2.next.next = ListNode(4)

# Expected: 1->1->2->3->4->4
print(m.mergeTwoLists(n1, n2))

# Expected: 1->2->4
print(m.mergeTwoLists(n1, None))

# Expected: 1->3->4
print(m.mergeTwoLists(None, n2))

# Expected: null
print(m.mergeTwoLists(None, None))
