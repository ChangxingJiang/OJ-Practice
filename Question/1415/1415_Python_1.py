class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        for i in range(n):
            v = 2 ** (n - i - 1)
            if i == 0:
                if k > 3 * v:
                    return ""
                if k > 2 * v:
                    ans.append("c")
                    k -= 2 * v
                elif k > v:
                    ans.append("b")
                    k -= v
                else:
                    ans.append("a")
            else:
                if k > v:
                    if ans[-1] == "a" or ans[-1] == "b":
                        ans.append("c")
                    else:
                        ans.append("b")
                    k -= v
                else:
                    if ans[-1] == "b" or ans[-1] == "c":
                        ans.append("a")
                    else:
                        ans.append("b")
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().getHappyString(n=1, k=3))  # "c"
    print(Solution().getHappyString(n=1, k=4))  # ""
    print(Solution().getHappyString(n=3, k=9))  # "cab"
    print(Solution().getHappyString(n=2, k=7))  # ""
    print(Solution().getHappyString(n=10, k=100))  # "abacbabacb"
