class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for x in nums:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                return True
        
        return False

        