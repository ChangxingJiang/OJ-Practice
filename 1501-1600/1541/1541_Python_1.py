class Solution:
    def minInsertions(self, s: str) -> int:
        # 用栈处理可以配对的括号
        N = len(s)
        ans = 0
        stack = []
        i = 0
        while i < N:
            if s[i] == "(":
                stack.append("(")
                i += 1
            else:
                if i < len(s) - 1 and s[i + 1] == ")":
                    i += 2
                else:  # 如果不是连续的括号则补一个使其成为连续的括号
                    i += 1
                    ans += 1
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")

        print(ans, stack)

        # 处理未配对的括号
        n1 = stack.count("(")
        n2 = len(stack) - n1
        ans += n1 * 2
        ans += n2

        return ans


if __name__ == "__main__":
    print(Solution().minInsertions(s="(()))"))  # 1
    print(Solution().minInsertions(s="())"))  # 0
    print(Solution().minInsertions(s="))())("))  # 3
    print(Solution().minInsertions(s="(((((("))  # 12
    print(Solution().minInsertions(s=")))))))"))  # 5
    print(Solution().minInsertions(s="()()()()()("))  # 7
    print(Solution().minInsertions(s="(()))(()))()())))"))  # 4
    print(Solution().minInsertions(s="))())())()())()))()))))(()))())))))(()()())()())((()())))()"))  # 19
