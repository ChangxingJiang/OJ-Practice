from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # 计算总消耗
        # O(N)
        ans = sum(task[0] for task in tasks)

        # 计算当前最大剩余量
        # O(N)
        # now = min(task[1] - task[0] for task in tasks)

        # 缩减剩余量
        # O(NlogN)
        surplus = [(task[1] - task[0], task[1]) for task in tasks]
        surplus.sort()

        # print(surplus)

        now = 0
        # now = surplus[]
        for s1, s2 in surplus:
            # print(now, s1, s2, "->", s1 - now if s1 > now else 0, "->", ans)
            if s1 > now:
                ans += s1 - now
                now = s1
            now += (s2 - s1)

        return ans


if __name__ == "__main__":
    print(Solution().minimumEffort([[1, 3], [1, 100]]))  # 100
    print(Solution().minimumEffort([[1, 2], [2, 4], [4, 8]]))  # 8
    print(Solution().minimumEffort([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))  # 32
    print(Solution().minimumEffort([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]))  # 27
    print(Solution().minimumEffort([[1, 2], [1, 7], [2, 3], [5, 9], [2, 2]]))  # 11
