class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        lst = [-1] * (n + 1)

        for i in range(n + 1):
            if i == 0:
                lst[i] = 0
            elif i == 1:
                lst[i] = 1

            elif i % 2 == 0:
                lst[i] = lst[i // 2]
            else:
                lst[i] = lst[i // 2] + lst[i // 2 + 1]

        return max(lst)


if __name__ == "__main__":
    print(Solution().getMaximumGenerated(7))  # 3
    print(Solution().getMaximumGenerated(2))  # 1
    print(Solution().getMaximumGenerated(3))  # 2
    print(Solution().getMaximumGenerated(4))  # 2
