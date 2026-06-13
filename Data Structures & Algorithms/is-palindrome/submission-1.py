class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        right = ""
        left = ""
        iteration = len(clean) // 2 # 9
        for i in range(0, iteration):
            left += clean[i]
            right += clean[len(clean) - 1 - i]
        return right == left




        
         
            

            



    
        

        