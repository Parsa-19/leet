class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
            
        print(f"k --> {k}")
        
        if k >= 1:

            nums_copy = [n for n in nums] 

            i = 0 
            for k_num in nums[-k:]:  
                nums[i] = k_num
                i += 1

            for before_k_num in nums_copy[:len(nums)-k]:
                nums[i] = before_k_num
                i += 1

        print(nums)



nums = [1, 2]
k = 7
solu = Solution()
res = solu.rotate(nums, k)