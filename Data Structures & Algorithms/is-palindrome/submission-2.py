class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        # O(N)
        for ch in s:
            valid_ch = self.isValidCharacter(ch)
            if valid_ch == False:
                continue
            clean += valid_ch
        
        l, r = 0, len(clean) - 1
        while l < r:
            left_ch, right_ch = clean[l], clean[r]
            if left_ch == right_ch:
                l += 1
                r -= 1
                continue
            else:
                return False
        return True

    
    def isValidCharacter(self, ch):
        if ch >= 'a' and ch <= 'z':
            return ch
        elif ch >= 'A' and ch <= 'Z':
            return ch.lower()
        elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
            return ch
        return False






        
         
            

            



    
        

        