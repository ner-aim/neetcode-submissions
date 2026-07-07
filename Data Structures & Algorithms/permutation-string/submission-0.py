class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Hash = [0] * 26

        for x in s1:
            s1Hash[ord(x) - ord("a")] += 1

        def helper(s):
            s2Hash = [0] * 26
            for x in s:
                s2Hash[ord(x) - ord("a")] += 1
            return s2Hash

        m = len(s1)
        n = len(s2)

        for i in range(n):
            j = i + m
            if j > n:
                return False

            if helper(s2[i:j]) == s1Hash:
                return True

        return False
