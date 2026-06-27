class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                res = self.evaluate(num2, num1, token)
                stack.append(res)
        return stack[-1]

    
    def evaluate(self, num1, num2, token):
        if token == "+":
            return num1 + num2
        elif token == "-":
            return num1 - num2
        elif token == "/":
            return int(num1 / num2)
        return num1 * num2

        