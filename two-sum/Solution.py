class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [-1, -1]
        dict = {}
        i = 0
        while i < len(nums):
            if dict.get(target - nums[i]) != None:
                ret[0] = dict.get(target - nums[i]) + 1
                ret[1] = i + 1
                return ret
            else:
                dict[nums[i]] = i
            i = i + 1

    def test(self):
        print ('test')
