class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Approach: using hash map 
        hash_map = {}
        for ch in s1:
            hash_map[ch] = hash_map.get(ch, 0) + 1
        
        for idx, ch in enumerate(s2):
            if ch in s1:
                if (idx + len(s1)) <= len(s2):
                    j = idx
                    temp_map = {}
                    end = idx + len(s1) - 1
                    while j <= end:
                        temp_map[s2[j]] = temp_map.get(s2[j], 0) + 1 
                        j += 1
                    if temp_map == hash_map:
                        return True
                else:
                    return False
        return False

        

        