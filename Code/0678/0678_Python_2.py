class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left_num = 0
        max_left_num = 0
        for ch in s:
            if ch == "(":
                min_left_num += 1
                max_left_num += 1
            elif ch == "*":
                if min_left_num > 0:
                    min_left_num -= 1
                max_left_num += 1
            else:
                if min_left_num > 0:
                    min_left_num -= 1
                max_left_num -= 1
            if max_left_num < 0:
                return False
        return min_left_num == 0


if __name__ == "__main__":
    print(Solution().checkValidString("()"))  # True
    print(Solution().checkValidString("(*)"))  # True
    print(Solution().checkValidString("(*))"))  # True
    print(Solution().checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))  # False
    print(Solution().checkValidString("(*()"))  # True
