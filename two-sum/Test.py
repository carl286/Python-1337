from Solution import Solution

def main():
    s = Solution()
    s.test()
    nums = [0,0]
    #nums = [0,4,3,0]
    target = 0
    print (s.twoSum(nums, target))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
