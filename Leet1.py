class Solution:
    def twoNum(self, nums, target): 
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rmap = dict()
        for i, num in enumerate(nums):
            if num in rmap:
                return [rmap[num], i]
            rmap[target - num] = i
        return
