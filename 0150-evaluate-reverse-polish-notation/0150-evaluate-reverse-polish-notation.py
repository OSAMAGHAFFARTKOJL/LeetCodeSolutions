class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def is_integer(s: str) -> bool:
            return s.isdigit() or (s[0] == '-' and s[1:].isdigit())

        for i in tokens:
            if is_integer(i):
                stack.append(int(i))
            else:
                element_2 = stack.pop()
                element_1 = stack.pop()

                if i == '+':
                    stack.append(element_1 + element_2)
                elif i == '-':
                    stack.append(element_1 - element_2)
                elif i == '*':
                    stack.append(element_1 * element_2)
                elif i == '/':
                    stack.append(int(element_1 / element_2))  # Truncate towards zero

        return stack[-1]
