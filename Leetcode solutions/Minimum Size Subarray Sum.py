class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        r=0
        l=0
        res = float("inf")

        while(r < n):
            sum += nums[r]

            if(sum>=target):
                while sum>=target:
                    sum -= nums[l]
                    l+=1
                res = min(res,r-l+2)
                
            r+=1

        return 0 if res==float("inf") else res
