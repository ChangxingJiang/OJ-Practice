import functools
from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # 依据街道位置排序房屋
        # O(NlogN)
        houses.sort()

        # 计算房屋间的距离
        distances = []
        for i in range(len(houses) - 1):
            distances.append(houses[i + 1] - houses[i])

        print(distances)

        # 递归函数
        @functools.lru_cache(None)
        def dfs(left, right, kk):
            # 处理人人安邮筒的特殊情况
            # O(1)
            if kk >= right - left + 1:
                return 0

            # 处理只有一个邮筒的特殊情况
            # O(N)
            if kk == 1:
                ans = 0
                for ii in range(1, (right - left + 1) // 2 + 1):
                    idx_left, idx_right = left + (ii - 1), right - (ii - 1) - 1
                    if idx_left != idx_right:
                        ans += (distances[idx_left] + distances[idx_right]) * ii
                    else:
                        ans += (distances[idx_left]) * ii
                        break
                return ans

            # 处理有多个邮筒的情况（递归处理）
            # 递归最左边的邮筒的安装位置
            ans = 0
            for ii in range(left, right + 1):

                return dfs(left + 1, right, kk - 1)

        # 递归处理所有可能的情况
        # O(NK)
        return dfs(left=0, right=len(distances), kk=k)


if __name__ == "__main__":
    print(Solution().minDistance(houses=[1, 4, 8, 10, 20], k=3))  # 5
    print(Solution().minDistance(houses=[2, 3, 5, 12, 18], k=2))  # 9
    print(Solution().minDistance(houses=[7, 4, 6, 1], k=1))  # 8
    print(Solution().minDistance(houses=[3, 6, 14, 10], k=4))  # 0
    print(Solution().minDistance(houses=[1, 2], k=1))  # 1
