class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        
        while numbers[left] + numbers[right]!=target:
            sum = numbers[left] + numbers[right]        
            if sum > target:
                right-=1
            else:
               left+=1 
        
        return [left + 1 , right + 1]
        