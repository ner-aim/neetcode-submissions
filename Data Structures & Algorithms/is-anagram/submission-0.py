class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMapS = defaultdict(int)
        hashMapT = defaultdict(int)

        n = len(s)

        for i in range(n):
            hashMapS[s[i]] += 1
            hashMapT[t[i]] += 1
        
        if hashMapS == hashMapT:
            return True
        
        return False
