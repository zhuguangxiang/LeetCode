'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode [2,4,3]
        :type l2: ListNode [5,0,6]
        :rtype: ListNode
        """

        def to_int(l):
            if l is None:
                return 0
            else:
                return l.val + 10 * to_int(l.next)

        def to_linkedlist(num):
            l = ListNode(num % 10)
            num = num // 10
            if num != 0:
                l.next = to_linkedlist(num)
            return l
        l1_num = to_int(l1)
        l2_num = to_int(l2)
        return to_linkedlist(l1_num + l2_num)


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(0)
    l2.next.next = ListNode(6)

    sol = Solution().addTwoNumbers(l1,l2)
    while sol:
        print(sol.val)
        sol = sol.next