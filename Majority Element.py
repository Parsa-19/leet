class Solution:
	def majorityElement(self, nums: list[int]) -> int:

		item_majority = nums[0] # hold the item with biggest majority
		number_of_existence_majority = 1 # hold number of majority for that item

		new_items = []
		total_majority_stat = {}

		for item in nums:

			if item not in new_items: 
				new_items.append(item)
				total_majority_stat[item] = 1 # add the new item as key and 1 time existence
				continue 
			
			total_majority_stat[item] += 1
			if number_of_existence_majority < total_majority_stat[item]:
				item_majority = item
				number_of_existence_majority = total_majority_stat[item]
				
	

		# print(total_majority_stat)
		# print()
		# print(f"item => {item_majority}")
		# print(f"number_of_existence {number_of_existence_majority}")
		
		return item_majority



nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
solu = Solution()
res = solu.majorityElement(nums)
print(res)
