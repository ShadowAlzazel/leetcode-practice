class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = 0
        len_nums = len(nums)
        search_index = min(len_nums, k + 1) 
        sub_list = nums[0:search_index]
        sub_set = set(sub_list)
        counter_max = len_nums - min(len_nums, k + 1) + 1

        while counter < counter_max:
            if len(sub_set) < len(sub_list):
                return True

            counter += 1
            if counter < counter_max:
                new_num = nums[k + counter]
                sub_list.append(new_num)
                sub_set.remove(sub_list[0])
                sub_list.pop(0)
                sub_set.add(new_num)
                

        return False