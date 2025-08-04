'''

<< 80. Remove Duplicates from Sorted Array II >>

'''


class Solution:
    def remove_third_and_more_of_a_same_item(self, first_appeare_index, nums):
        main_nums = nums
        main_list_len = len(main_nums) 
        compare_num = main_nums[first_appeare_index]

        i = 0
        for num_index in range(first_appeare_index, main_list_len):
            
            each_num = main_nums[num_index] 
            if each_num != compare_num: # heat the edge of same items
                break
            
            if i >= 2: # keep two items and then make same items all none
                main_nums[num_index] = None
            
            i += 1

        return main_nums


    def find_all_first_appear_index(self, nums) -> list: # returns a list of indexes
        new_appeare_indexes = [0] # zero is always the index that shows the first appearence of first item
        
        compare_number = nums[0]
        i = 0
        for number in nums:
            if compare_number != number:
                compare_number = number
                new_appeare_indexes.append(i) 
            i += 1

        return new_appeare_indexes


    def removeDuplicates(self, nums: list[int]) -> int:
        # first_appearence_index:  0      3        7  8             remove_items:   0 1 1 3
        #                         [0,0,0, 1,1,1,1, 2, 3,3,3]  => [0,0, 1,1, 2, 3,3, _,_,_,_]

        if not nums:
            return 0

        # 1. find all indexes relating to first appearence of each new item in list 
        all_first_appeare_indexes = self.find_all_first_appear_index(nums)


        # 2. keep two items of each number in list and assign 'None' to rest of them 
        for first_appeare_index in all_first_appeare_indexes:
            nums = self.remove_third_and_more_of_a_same_item(first_appeare_index, nums)
            print(nums)

        
        # 3. remove all 'None' items
        nums = [item for item in nums if item is not None]
        return nums


        


        


nums = [1,1,1,2,2,3]
solu = Solution()
res = solu.removeDuplicates(nums)
print(f'\n\n{res}')