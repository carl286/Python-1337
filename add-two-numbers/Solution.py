class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def test(self):
        print ('test')

    def addTwoNumbersHelper(self, l1, l2, carryon):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type carryon: int
        :rtype: ListNode
        """
        if not l1 and not l2:
            if carryon:
                return ListNode(carryon)
            else:
                return None

        ret = ListNode(carryon)
        l1_next = None
        l2_next = None

        if l1:
            ret.val += l1.val
            l1_next = l1.next

        if l2:
            ret.val += l2.val
            l2_next = l2.next

        if ret.val >= 10:
            ret.val -= 10
            carryon = 1
        else:
            carryon = 0
        
        next = self.addTwoNumbersHelper(l1_next, l2_next, carryon)
        ret.next = next

        return ret

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #return self.addTwoNumbersHelper(l1, l2, 0)
        if not l1:
            return l2
        if not l2:
            return l1

        carryon = 0
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            l1.val = l2.val + l1.val + carryon
            if l1.val >= 10:
                l1.val -= 10
                carryon = 1
            else:
                carryon = 0
            tail.next = l1
            tail = l1
            l1 = l1.next
            l2 = l2.next

        while l2:
            l2.val += carryon
            if l2.val >= 10
                l2.val -= 10
                carryon = 1
            else
                carryon = 0
            tail.next = l2
            tail = l2
            l2 = l2.next

        while l1:
            l1.val += carryon
            if l1.val >= 10:
                l1.val -= 10
                carryon = 1
            else:
                carryon = 0
            tail.next = l1
            tail = l1
            l1 = l1.next

        if carryon:
            tail.next = ListNode(carryon)
        return dummy.next
