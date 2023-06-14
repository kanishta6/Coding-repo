class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        count = 0
        for i in nums:
            if count<2 or i!=nums[count-2]:
                nums[count] = i
                count+=1
        return count