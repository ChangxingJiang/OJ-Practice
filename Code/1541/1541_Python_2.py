class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        ans = 0
        left_num = 0
        i = 0
        while i < N:
            if s[i] == "(":
                left_num += 1
                i += 1
            else:
                if i < len(s) - 1 and s[i + 1] == ")":
                    i += 2
                else:  # 如果不是连续的括号则补一个使其成为连续的括号
                    i += 1
                    ans += 1
                if left_num > 0:
                    left_num -= 1
                else:
                    ans += 1

        return ans + 2 * left_num


if __name__ == "__main__":
    print(Solution().minInsertions(s="(()))"))  # 1
    print(Solution().minInsertions(s="())"))  # 0
    print(Solution().minInsertions(s="))())("))  # 3
    print(Solution().minInsertions(s="(((((("))  # 12
    print(Solution().minInsertions(s=")))))))"))  # 5
    print(Solution().minInsertions(s="()()()()()("))  # 7
    print(Solution().minInsertions(s="(()))(()))()())))"))  # 4
    print(Solution().minInsertions(s="))())())()())()))()))))(()))())))))(()()())()())((()())))()"))  # 19
