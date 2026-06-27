class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                res = self.evaluate(left, right, token)
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

        