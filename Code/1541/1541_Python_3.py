class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "*")
        ans = s.count(")")
        s = s.replace(")", "*")
        while len(ss := s.replace("(*", "")) != len(s):
            s = ss
        return ans + len(s) + s.count("(")


if __name__ == "__main__":
    print(Solution().minInsertions(s="(()))"))  # 1
    print(Solution().minInsertions(s="())"))  # 0
    print(Solution().minInsertions(s="))())("))  # 3
    print(Solution().minInsertions(s="(((((("))  # 12
    print(Solution().minInsertions(s=")))))))"))  # 5
    print(Solution().minInsertions(s="()()()()()("))  # 7
    print(Solution().minInsertions(s="(()))(()))()())))"))  # 4
    print(Solution().minInsertions(s="))())())()())()))()))))(()))())))))(()()())()())((()())))()"))  # 19
