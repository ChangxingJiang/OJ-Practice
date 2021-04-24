from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def maxHappyGroups(self, batch_size: int, groups: List[int]) -> int:
        if batch_size == 1:
            return len(groups)

        ans = 0

        count = [0] * batch_size  # 统计每种余数的数量
        for group in groups:
            remainder = group % batch_size
            if remainder == 0:
                ans += 1
            else:
                count[remainder] += 1

        # 所有可以除尽的组最先安排，一定都是开心的
        def dfs(stat, rest):
            key = (tuple(stat), rest)
            if key in self.cache:
                return self.cache[key]

            res = 0
            for i in range(1, batch_size):
                if stat[i] > 0:
                    stat[i] -= 1
                    if rest == 0:
                        res = max(res, dfs(stat, (rest + i) % batch_size) + 1)
                    else:
                        res = max(res, dfs(stat, (rest + i) % batch_size))
                    stat[i] += 1

            self.cache[key] = res

            return res

        return ans + dfs(count, 0)


if __name__ == "__main__":
    print(Solution().maxHappyGroups(batch_size=3, groups=[1, 2, 3, 4, 5, 6]))  # 4
    print(Solution().maxHappyGroups(batch_size=4, groups=[1, 3, 2, 5, 2, 2, 1, 6]))  # 4

    # 16
    print(Solution().maxHappyGroups(
        batch_size=8,
        groups=[8, 8, 4, 1, 6, 8, 6, 3, 7, 7, 2, 4, 1, 6, 7, 4, 1, 4, 2, 4, 4, 7, 6, 1, 5, 1, 3, 4, 1, 1]))

    # 自制测试用例
    # print(Solution().maxHappyGroups(batchSize=9, groups=[1, 5, 7]))  # 1
    # print(Solution().maxHappyGroups(batchSize=5, groups=[1, 2, 3, 3, 3, 3, 3, 4, 5, 6]))  # 5
    # print(Solution().maxHappyGroups(batchSize=5, groups=[1, 2, 3, 4, 5, 6, 1, 2, 1, 2]))  # 5
    # print(Solution().maxHappyGroups(batchSize=5, groups=[1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]))  # 3
