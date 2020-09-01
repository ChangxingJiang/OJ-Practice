class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        mark_sign = []
        stack = [[]]
        for ch in expression:
            if ch == "!" or ch == "|" or ch == "&":
                mark_sign.append(ch)
                stack.append([])
            elif ch == ")":
                mark = mark_sign.pop()
                now = stack.pop()
                if mark == "!":
                    tmp = not now[0]
                elif mark == "&":
                    tmp = all(now)
                else:
                    tmp = any(now)
                stack[-1].append(tmp)
            elif ch == "t":
                stack[-1].append(True)
            elif ch == "f":
                stack[-1].append(False)
        return stack[0][0]


if __name__ == "__main__":
    print(Solution().parseBoolExpr(expression="!(f)"))  # True
    print(Solution().parseBoolExpr(expression="|(f,t)"))  # True
    print(Solution().parseBoolExpr(expression="&(t,f)"))  # False
    print(Solution().parseBoolExpr(expression="|(&(t,f,t),!(t))"))  # False
    print(Solution().parseBoolExpr(expression="&(t,t,t)"))  # True
