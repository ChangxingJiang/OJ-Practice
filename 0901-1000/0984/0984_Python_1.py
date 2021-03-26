class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = []
        while A or B:
            if len(ans) >= 2 and ans[-2] == ans[-1]:
                if ans[-1] == "a":
                    ans.append("b")
                    B -= 1
                else:
                    ans.append("a")
                    A -= 1
            elif A > B:
                ans.append("a")
                A -= 1
            else:
                ans.append("b")
                B -= 1

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().strWithout3a3b(1, 2))  # "abb"
    print(Solution().strWithout3a3b(4, 2))  # "aabaa"
