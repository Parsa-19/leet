def insertion_sort(nums_list):
    
    for i in range(1, len(nums_list)):
        
        temp = nums_list[i]
        j = i - 1

        while j >= 0 and nums_list[j] > temp:
            nums_list[j + 1] = nums_list[j] 
            j -= 1

        nums_list[j + 1] = temp




insertion_sort([4, 7, 1, 3, 2, 9, 6, 8, 5])