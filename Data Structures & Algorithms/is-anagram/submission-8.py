class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        hashmap1 = {}
        hashmap2 = {}

        for i in range(0, len(s)):
            hashmap1[s[i]] = hashmap1.get(s[i], 0) + 1
            hashmap2[t[i]] = hashmap2.get(t[i], 0) + 1
        
        for ch in s:
            if ch not in hashmap2:
                return False
            if hashmap1[ch] != hashmap2[ch]:
                return False
        
        return True



        