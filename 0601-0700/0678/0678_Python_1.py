class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == ")":
                idx = len(stack) - 1
                while idx > -1:
                    if stack[idx] == "(":
                        break
                    idx -= 1
                if idx >= 0:
                    stack.pop(idx)
                elif len(stack) > 0:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        left_num = 0
        for ch in stack:
            if ch == "(":
                left_num += 1
            elif left_num > 0:
                left_num -= 1
        return left_num == 0


if __name__ == "__main__":
    print(Solution().checkValidString("()"))  # True
    print(Solution().checkValidString("(*)"))  # True
    print(Solution().checkValidString("(*))"))  # True
    print(Solution().checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))  # False
    print(Solution().checkValidString("(*()"))  # True
