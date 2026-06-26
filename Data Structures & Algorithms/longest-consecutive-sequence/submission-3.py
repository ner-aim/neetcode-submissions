class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        longest = 0
        numSet = set(nums)
        for number in numSet:
            if number - 1 not in numSet:
                length = 1
                while number + length in numSet:
                    length += 1
                longest = max(length, longest)
            
        return longest
            
