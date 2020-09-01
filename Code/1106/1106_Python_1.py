class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = [[]]
        i = 0
        while i < len(expression):
            ch = expression[i]
            if ch == "!" or ch == "|" or ch == "&":
                stack.append([ch])
                i += 1
            elif ch == ")":
                now = stack.pop()
                if now[0] == "!":
                    tmp = not now[1]
                elif now[0] == "&":
                    tmp = all(now[1:])
                else:
                    tmp = any(now[1:])
                stack[-1].append(tmp)
            elif ch == "t":
                stack[-1].append(True)
            elif ch == "f":
                stack[-1].append(False)
            i += 1
            print(stack)
        return stack[0][0]


if __name__ == "__main__":
    print(Solution().parseBoolExpr(expression="!(f)"))  # True
    print(Solution().parseBoolExpr(expression="|(f,t)"))  # True
    print(Solution().parseBoolExpr(expression="&(t,f)"))  # False
    print(Solution().parseBoolExpr(expression="|(&(t,f,t),!(t))"))  # False
    print(Solution().parseBoolExpr(expression="&(t,t,t)"))  # True
