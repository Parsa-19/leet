class Solution:
    def get_the_int_prifix_between_two_intigers(self, num1, num2):
        if num1 >= 1 and num2 >= 1:
            smaller_num_len = num1 if num1 < num2 else num2 # get the smalles length of these numbers 

            num1 = str(num1)
            num2 = str(num2)
            smaller_num_len = str(smaller_num_len)

            prifix = ''
            for i in range(len(smaller_num_len)):
                if num1[i] == num2[i]:
                    prifix += num1[i] # no matter which one
                    continue
                break

            return int(prifix) if prifix else None 

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        all_prifixes = []
        for i in arr1:
            for j in arr2:
                prifix = self.get_the_int_prifix_between_two_intigers(i, j)
                if prifix:
                    all_prifixes.append(prifix)
        
        if len(all_prifixes) >= 1:
            max_prif = all_prifixes[0]
            for prif in all_prifixes:
                if prif > max_prif:
                    max_prif = prif
            
            return len(str(max_prif))
                    
        return 0


        
if __name__ == "__main__":
    solu = Solution()
    print(solu.longestCommonPrefix([13,27,45], [21,27,48]))

