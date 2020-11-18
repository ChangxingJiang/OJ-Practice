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
        print("距离列表:", distances)

        # 处理特殊情况
        if k == len(houses):
            return 0

        # 计算范围内只有一个邮筒的距离情况
        def count(dds):
            if not dds:
                return 0
            if len(dds) == 1:
                return dds[0]
            res = 0
            idx = 1
            while True:
                idx_left, idx_right = idx - 1, len(dds) - idx
                if idx_left < idx_right:
                    res += (distances[idx_left] + distances[idx_right]) * idx
                    idx += 1
                elif idx_left == idx_right:
                    res += (distances[idx_left]) * idx
                    break
                else:
                    break
            return res

        # 处理只安装一个邮筒的情况
        if k == 1:
            return count(distances)

        # 计算拆分位置
        use_distance = list(sorted(distances))[:-(k - 1)]
        print("拆分长度:", use_distance)

        # 计算最终结果
        ans = 0
        now = []
        for d in distances:
            if d in use_distance:
                now.append(d)
                use_distance.remove(d)
            else:
                ans += count(now)
                now = []
        ans += count(now)

        return ans


if __name__ == "__main__":
    print(Solution().minDistance(houses=[1, 4, 8, 10, 20], k=3))  # 5
    print(Solution().minDistance(houses=[2, 3, 5, 12, 18], k=2))  # 9
    print(Solution().minDistance(houses=[7, 4, 6, 1], k=1))  # 8
    print(Solution().minDistance(houses=[3, 6, 14, 10], k=4))  # 0
    print(Solution().minDistance(houses=[1, 2], k=1))  # 1
    print(Solution().minDistance(houses=[1, 8, 12, 10, 3], k=3))  # 4
    print(Solution().minDistance(houses=[14, 2, 5, 7, 10], k=2))  # 9
