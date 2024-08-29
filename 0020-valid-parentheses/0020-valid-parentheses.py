class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hsh = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s: 
            if i in hsh:
                top = stack.pop() if stack else "#"
                if top != hsh[i]:
                    return False

            else:
                stack.append(i)
        return not stack



       