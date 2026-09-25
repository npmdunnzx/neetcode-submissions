class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        for tok in tokens:
            if tok in ['+','-','*','/']:
                a = temp.pop()
                b = temp.pop()
                if tok == '+':
                    temp.append(b + a)
                elif tok == '-':
                    temp.append(b - a)
                elif tok == '*':
                    temp.append(b * a)
                elif tok == '/':
                    temp.append(int(b/a))
            else:
                temp.append(int(tok))
        return temp[0]