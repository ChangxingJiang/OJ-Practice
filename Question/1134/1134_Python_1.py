class Solution:
    def isArmstrong(self, N: int) -> bool:
        lst = [int(ch) for ch in str(N)]
        ans = 0
        size = len(lst)
        for i in range(size):
            ans += lst[i] ** size
        return ans == N


if __name__ == "__main__":
    print(Solution().isArmstrong(153))  # True
    print(Solution().isArmstrong(123))  # False
