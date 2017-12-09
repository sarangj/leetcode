class Solution:
    def twoNum(self, nums, target): 

        rmap = dict()
        for i, num in enumerate(nums):
            if num in rmap:
                return [rmap[num], i]
            if num <= target:
                rmap[target - num] = i
        return
