from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 生成用分钟表示的时间
        lst = []
        for time in timePoints:
            hour, minute = time.split(":")
            lst.append(int(hour) * 60 + int(minute))

        # 排序时间列表
        lst.sort()

        # 计算最小时间差
        ans = lst[0] + 1440 - lst[-1]  # 首尾相差一天的最小值
        for i in range(len(lst) - 1):
            ans = min(ans, lst[i + 1] - lst[i])
        return ans


if __name__ == "__main__":
    print(Solution().findMinDifference(["23:59", "00:00"]))  # 1
