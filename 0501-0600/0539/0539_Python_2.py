from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 生成用分钟表示的时间
        lst = set()
        for time in timePoints:
            minute = int(time[:2]) * 60 + int(time[3:])
            if minute in lst:
                return 0
            lst.add(minute)

        # 排序时间列表
        lst = sorted(lst)

        # 考虑跨午夜的情况
        lst.append(lst[0] + 1440)

        # 计算最小时间差
        return min(lst[i + 1] - lst[i] for i in range(len(lst) - 1))


if __name__ == "__main__":
    print(Solution().findMinDifference(["23:59", "00:00"]))  # 1
