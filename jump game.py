class Solution:
    def canJump(self, nums: list[int]) -> bool:

        def jump_recursively(nums, current_ind):
            
            if len(nums) == 1:
                return True

            nums = nums[:current_ind] # remove items before the current index 
            
            current_value = nums[current_ind]
            if not current_value # if the current value is 0 then it should step back or 
                if current_ind == 0: # if it is the first position return false
                    return False
                current_ind -= 1

            current_ind += nums[current_ind] # then add value of current item to the next index we want to jump




        jump_recursively(nums, 0)



solu = Solution()
res = solu.canJump([2,3,1,1,4])
if res:
    print(f'\nres:\n{res}')



# generators
# iterators
# scopes
# list comperhesions
# recursive functions
# lambda
# map() filter()