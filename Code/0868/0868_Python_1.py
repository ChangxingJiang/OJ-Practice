class Solution:
    def binaryGap(self, N: int) -> int:
        N = bin(N)

        ans = 0
        start = -1
        for i in range(len(N)):
            if N[i] == "1":
                if start != -1:
                    ans = max(ans, i - start)
                start = i
        return ans


if __name__ == "__main__":
    print(Solution().binaryGap(22))  # 2
    print(Solution().binaryGap(5))  # 2
    print(Solution().binaryGap(6))  # 1
    print(Solution().binaryGap(8))  # 0
