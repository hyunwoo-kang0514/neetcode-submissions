class Solution:
    def isValid(self, s: str) -> bool:
       # Create a stack
       stack = []
       # Create a match dict
       openToClose = {"(" : ")", "[" : "]", "{" : "}"}
       for c in s:
            if c in openToClose: # ({{[
                stack.append(c)
            elif len(stack) != 0 and openToClose[stack[-1]] != c:
                return False
            elif len(stack) == 0 and c in openToClose.values():
                return False
            elif len(stack) != 0 and openToClose[stack[-1]] == c:
                stack.pop()
        
       if len(stack) == 0:
            return True
       return False

       
            
            

            

        