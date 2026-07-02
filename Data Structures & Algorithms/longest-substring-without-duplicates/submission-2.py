class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        wordLength = 0
        characters = set()

        n = len(s)
        for j in range(n):
            while s[j] in characters:
                characters.remove(s[i])
                i += 1

            characters.add(s[j])
            w = j - i + 1
            wordLength = max(w, wordLength)
   
        return wordLength
