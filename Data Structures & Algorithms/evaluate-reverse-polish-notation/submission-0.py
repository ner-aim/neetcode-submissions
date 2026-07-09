class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        n = len(tokens)
        for i in range(n):
            if tokens[i] not in ["+", "*", "/", "-"]:
                stack.append(int(tokens[i]))
            else:
                second = stack.pop()
                first = stack.pop()

                if tokens[i] == "+":
                    stack.append(int(first + second))
                elif tokens[i] == "*":
                    stack.append(int(first * second))
                elif tokens[i] == "/":
                    stack.append(int(first / second))
                elif tokens[i] == "-":
                    stack.append(int(first - second))

        return int(stack.pop())
