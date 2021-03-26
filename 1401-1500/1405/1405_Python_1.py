class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        a, b, c = min(a, 2 * (b + c + 1)), min(b, 2 * (a + c + 1)), min(c, 2 * (a + b + 1))

        ans = ["", ""]
        while a > 0 or b > 0 or c > 0:
            v1, v2, v3 = sorted([a, b, c], reverse=True)
            if v1 == a:
                if ans[-2] != "a" or ans[-1] != "a":
                    ans.append("a")
                    a -= 1
                else:
                    if v2 == b:
                        ans.append("b")
                        b -= 1
                    else:
                        ans.append("c")
                        c -= 1
            elif v1 == b:
                if ans[-2] != "b" or ans[-1] != "b":
                    ans.append("b")
                    b -= 1
                else:
                    if v2 == a:
                        ans.append("a")
                        a -= 1
                    else:
                        ans.append("c")
                        c -= 1
            else:
                if ans[-2] != "c" or ans[-1] != "c":
                    ans.append("c")
                    c -= 1
                else:
                    if v2 == a:
                        ans.append("a")
                        a -= 1
                    else:
                        ans.append("b")
                        b -= 1

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().longestDiverseString(1, 1, 7))  # "ccaccbcc"
    print(Solution().longestDiverseString(2, 2, 1))  # "aabbc"
    print(Solution().longestDiverseString(7, 1, 0))  # "aabaa"
