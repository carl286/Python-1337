from Solution import Solution
from Solution import ListNode 

def main():
    s = Solution()
    s.test()
    l1 = ListNode(1)
    l2 = ListNode(2)
#    print (s.addTwoNumbersHelper(l1, l2,0).val)
    print (s.addTwoNumbers(l1, l2).val)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
