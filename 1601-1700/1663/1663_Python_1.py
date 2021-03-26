class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        ans = [1] * n
        i = n - 1
        while k:
            if k > 25:
                ans[i] = 26
                k -= 25
            else:
                ans[i] = 1 + k
                k = 0
            i -= 1

        return "".join(chr(i + 96) for i in ans)

if __name__ == "__main__":
    print(Solution().getSmallestString(3, 27))  # aay
    print(Solution().getSmallestString(5, 73))  # aaszz
