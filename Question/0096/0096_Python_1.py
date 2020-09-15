class Solution:
    def numTrees(self, n: int) -> int:
        lst = [0] * (n + 1)
        lst[0], lst[1] = 1, 1  # 当有0个或1个结点时有1种可能

        for i in range(2, n + 1):  # 从2开始迭代计算
            for j in range(i):
                lst[i] += lst[j] * lst[i - 1 - j]

        return lst[-1]


if __name__ == "__main__":
    print(Solution().numTrees(3))  # 5
