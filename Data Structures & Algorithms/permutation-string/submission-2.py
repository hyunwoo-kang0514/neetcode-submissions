class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for ch in s1:
            s1_map[ch] = s1_map.get(ch, 0) + 1
        i = 0
        while i < len(s2):
            end = i + len(s1)
            if end <= len(s2):
                j = i
                s2_map = {}
                while j <= end - 1:
                    s2_map[s2[j]] = s2_map.get(s2[j], 0) + 1
                    j += 1
                if s2_map == s1_map:
                    return True
            else:
                return False
            i += 1
        return False


        

        