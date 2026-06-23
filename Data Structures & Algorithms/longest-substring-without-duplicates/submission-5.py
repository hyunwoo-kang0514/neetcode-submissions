class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currString = ""
        maxL = 0
        for ch in s:
            if ch not in currString:
                currString += ch
            else:
                maxL = max(maxL, len(currString))
                idx = currString.index(ch)
                currString = currString[idx + 1:] + ch
        return max(maxL, len(currString))