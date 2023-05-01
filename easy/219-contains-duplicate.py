# Failed 
#class Solution:
#    def containsDuplicate(self, nums: List[int]) -> bool:
#        print(list(set(nums)))
#        print(nums)
#        return list(set(nums)) != nums

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    
# Since a set only has unique elements, if it is less than
# the originial, it must have a duplicate.