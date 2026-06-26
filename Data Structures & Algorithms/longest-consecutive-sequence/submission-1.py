class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        longest = 0
        for number in sorted(nums):
            if (number-1) in hashMap:
                hashMap[number] = hashMap[number-1] + 1
            else:
                hashMap[number] = 1
            if hashMap[number] > longest:
                longest = hashMap[number]
            
        return longest
            
