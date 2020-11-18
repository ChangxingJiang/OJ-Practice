from typing import List


class Node:
    def __init__(self, day, left, right):
        self.day = day
        self.left = left
        self.right = right


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        size = len(bloomDay)
        need_num = m * k

        # 处理花的总数不够的情况
        if size < need_num:
            return -1

        # 处理花的总数刚好够的情况
        if size == need_num:
            return max(bloomDay)

        # 寻找理论值
        # O(NlogN)
        sorted_bloom_day = list(sorted(bloomDay))
        threshold = sorted_bloom_day[need_num - 1]

        # 计算每一个连续花段
        # O(N)
        now_bloom = 0  # 当前已有的花束数量
        part_list = [0]  # 每一段阈值之下的长度
        day_list = []  # 每一段阈值之下间隔的阈值之上的天数

        for day in bloomDay:
            # 处理在阈值之下的天数
            if day <= threshold:
                part_list[-1] += 1
                if part_list[-1] >= k:
                    part_list[-1] -= k
                    now_bloom += 1

            # 处理在阈值之上的天数
            else:
                part_list.append(0)
                day_list.append(day)

        # 已经满足要求的情况
        if now_bloom >= m:
            return threshold

        # 排序逐个断点天数上升列表
        # O(N)
        day_ordered_list = list(sorted(set(day_list), reverse=True))

        # 逐个天数上升
        # O(N^2) O(N)
        while now_bloom < m:
            now = day_ordered_list.pop()

            # print(now, ":", now_bloom, part_list, day_list)

            new_part_list = [part_list[0]]
            new_day_list = []

            for i in range(len(day_list)):
                if day_list[i] == now:
                    new_part_list[-1] += 1 + part_list[i + 1]
                    if new_part_list[-1] >= k:
                        new_part_list[-1] -= k
                        now_bloom += 1
                else:
                    new_part_list.append(part_list[i + 1])
                    new_day_list.append(day_list[i])

            part_list = new_part_list
            day_list = new_day_list

            if now_bloom >= m:
                return now

        return -1


if __name__ == "__main__":
    print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))  # 3
    print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))  # -1
    print(Solution().minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))  # 12
    print(Solution().minDays(bloomDay=[1000000000, 1000000000], m=1, k=1))  # 1000000000
    print(Solution().minDays(bloomDay=[1, 10, 2, 9, 3, 8, 4, 7, 5, 6], m=4, k=2))  # 9
    print(Solution().minDays(bloomDay=[62, 75, 98, 63, 47, 65, 51, 87, 22, 27, 73, 92, 76, 44, 13, 90, 100, 85], m=2,
                             k=7))  # 98
