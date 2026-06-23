class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def hash_helper(string):
            hashMap = [0] * 26

            for x in string:
                hashMap[ord(x) - ord('a')] += 1
            return hashMap
        
        hashString = defaultdict(list)

        for string in strs:
            key = tuple(hash_helper(string))
            hashString[key].append(string)
        return list(hashString.values())
        