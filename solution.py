from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        #HashMap Approach
        
        #Create a hash map where key= number and value=#of appearances.
        elements = dict({})
        
        #majority flag
        flag = len(nums)/2
        majority = nums[0]
        
        #Loop though elements saving them in hash map and also checking if values is greater than n/2
        for num in nums:
            
            #check if element is in hash and if it's more than majority flag
            if num in elements:
                elements[num] = elements[num]+1
                
                if elements[num] > flag:
                    return num
            else:
                #add element to hash
                elements[num] = 1
                    
        return majority