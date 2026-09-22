class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for a in s:
            if a in ['(', '{', '[']:
                temp.append(a)
            else:
                if not temp:
                    return False
                last = temp[-1]
                if (last == '(' and a == ')') or (last == '{' and a == '}') or (last == '[' and a == ']'):
                    temp.pop()
                else:
                    return False                    
        return len(temp) == 0