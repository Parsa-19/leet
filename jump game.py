class Solution:
    def canJump(self, nums: list[int]) -> bool:
        print(nums)
        print()

        jumped = 0
        start_pos = 0

        while True:

            if jumped >= len(nums) - 1:
                return True

            if nums[jumped] == 0:
                start_pos += 1
                print("start pos changed")
                jumped = start_pos

            

            print(nums[jumped])
            jumped += nums[jumped]

            if start_pos >= len(nums) - 1:
                return False
            


solu = Solution()
# nums = [2,5,0,0]
# nums = [1,3, 44,44, 2, 33, 0, 44]
nums = [3,2,1,0,4]
print(f'\n{solu.canJump(nums)}')