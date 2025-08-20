



i = 0
def canJump(nums):



    def jump(nums, jump_length):        
        
        print(nums)
        print(jump_length)
        print()

        # global i
        # i += 1
        # if i == 4:
        #     print(0 - 1)
        #     return None

        if (len(nums) - jump_length) == 1: # jump == last-item
            return True

        elif jump_length >= len(nums): # jump > last-item
            nums = nums[jump_length:]
            return jump(nums, nums[0]-1) # decrease jump by one and jump again

        else: # jump < last-item
            
            # if nums[0] == 0 or nums[0] == 1:

            nums = nums[jump_length:]
            return jump(nums, nums[0])




    print(jump(nums, 0))





canJump([3,2,1,0,4])