class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"{" : "}", "[" : "]", "(" : ")"}
        for c in s:
            if c in openToClose:
                stack.append(c)
            elif len(stack) == 0 and c in openToClose.values():
                return False
            else: # 일단 여는 괄호가 아님, 그리고 stack이 비어잇고 닫는 괄호가 아님 남는 분기는 
                  # 스택이 차있고, c가 닫는괄호
                if openToClose.get(stack[-1]) != c:
                    return False
                stack.pop()

        return len(stack) == 0
                

       
            
            

            

        