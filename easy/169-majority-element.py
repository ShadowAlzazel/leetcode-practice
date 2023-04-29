class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums_dict = {x: nums.count(x) for x in set(nums)}
        num_max = 0
        index_max = 0 
        for x, y in nums_dict.items():
            if y > num_max:
                num_max = y
                index_max = x

        return index_max