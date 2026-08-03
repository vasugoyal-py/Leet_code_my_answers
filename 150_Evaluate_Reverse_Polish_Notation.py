class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lis = []
        for element in tokens:
            if element not in ['+', '-', '*', '/']:
                lis.append(int(element))
            else:
                x, y = lis.pop(), lis.pop()
                if element == '+':
                    lis.append(y + x)
                elif element == '-':
                    lis.append(y - x)
                elif element == '*':
                    lis.append(y * x)
                elif element == '/':
                    lis.append(int(y / x))
        z = lis.pop()
        return z