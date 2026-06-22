class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        substring = ""

        for ch in s:
            if ch not in substring:
                substring += ch
            else:
                maxL = max(maxL, len(substring))

                idx = substring.index(ch)
                substring = substring[idx + 1:] + ch

        return max(maxL, len(substring))