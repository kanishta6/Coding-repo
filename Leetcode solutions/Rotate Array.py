class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n  # Calculate the effective rotation index

        # Reverse the entire array
        reverse(nums, 0, n - 1)
    
        # Reverse the first k elements
        reverse(nums, 0, k - 1)
    
        # Reverse the remaining n - k elements
        reverse(nums, k, n - 1)