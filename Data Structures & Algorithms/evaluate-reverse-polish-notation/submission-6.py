class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            # numbers
            if token not in operators:
                stack.append(int(token))
            # operators
            else: 
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(self.evaluate(left, right, token))
        return int(stack.pop())
    

    def evaluate(self, left, right, operator):
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "/":
            return left / right
        return left * right



        