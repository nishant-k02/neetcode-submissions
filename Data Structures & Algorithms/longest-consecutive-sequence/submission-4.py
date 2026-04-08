from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))  # Remove duplicates and sort
        max_length = 0
        count = 1  # Start with a count of 1 for the first number in a sequence
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1  # Continue the consecutive sequence
            else:
                max_length = max(max_length, count)  # Update max_length if needed
                count = 1  # Reset count for a new sequence
        
        # Final check in case the longest sequence is at the end
        max_length = max(max_length, count)
        
        return max_length
