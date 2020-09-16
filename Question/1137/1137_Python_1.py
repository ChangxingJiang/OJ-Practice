class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0, 1, 1]
        for i in range(3, n + 1):
            ans.append(ans[-3] + ans[-2] + ans[-1])
        return ans[n]


if __name__ == "__main__":
    print(Solution().tribonacci(n=0))  # 0
    print(Solution().tribonacci(n=4))  # 4
    print(Solution().tribonacci(n=25))  # 1389537
