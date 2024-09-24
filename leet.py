class Solution(object):

    def __init__(self):
        self.rand_nums = [0, 4, 3, 2, 1, 13, 11, 12, 10,     21, 23, 22, 20,     123, 121, 122, 120,     113, 111, 112, 110, 133, 131, 132, 130] # a test list
        self.ordered_nums = []


    '''
    one thing this function does is: 
    it converts list numbers to string (make each item a string to be able to access digits by index)
    '''
    def get_rand_numbers(self):  
        temp_rand_nums = []
        for num in self.rand_nums:
            temp_rand_nums.append(str(num))
        return temp_rand_nums


    def order(self):

        nums = self.get_rand_numbers()

        # zero item check
        if '0' in nums:
            self.ordered_nums.append(['0']) 


        '''
        first index ordering
        '''
        char_index = 0
        # get all numbers starts with 1-9 in seprated lists and store them in self.ordered_numbers -> [[start with 1], [start with 2],..,[start with 9]]
        for j in range(1, 4):

            nums_with_same_first_index = []
            for num in nums:

                if num[char_index] == str(j):
                    nums_with_same_first_index.append(num)

            self.ordered_nums.append(nums_with_same_first_index)
        



        '''
        second index ordering
        '''
        char_index = 1
        for j in range(1, 4):

            for nums in self.ordered_nums:
                nums_with_same_second_index = []
                for num in nums:
                    
                    # if len(num) != 1: 
                        if num[char_index] == str(j):
                            nums_with_same_second_index.append(num)
                            print('shiit')

                self.ordered_nums.append(nums_with_same_first_index)
        


    def findKthNumber(self, n: int, k: int) -> list:
        return 0





    def display(self):
        for tiny_list in self.ordered_nums:
            print(tiny_list)

# if __name__ == "__main__":
solu = Solution()
solu.order()
solu.display()

print('done')