from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 处理特殊情况
        if m == 2:
            return max(position) - min(position)

        position.sort()

        # 计算距离列表
        distances = []
        for i in range(len(position) - 1):
            distances.append(position[i + 1] - position[i])

        # print(distances)

        # 检查指定值能否成功
        def check(v):
            find = 0
            now = 0
            for d in distances:
                now += d
                if now >= v:
                    find += 1
                    now = 0
                if find >= m - 1:
                    return True
            return False

        # 二分查找结果
        left = 0
        right = position[-1] - position[0]

        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == "__main__":
    print(Solution().maxDistance(position=[1, 2, 3, 4, 7], m=3))  # 3
    print(Solution().maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))  # 999999999
    print(Solution().maxDistance(position=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], m=4))  # 3
