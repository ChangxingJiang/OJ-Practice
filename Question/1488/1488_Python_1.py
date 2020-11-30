import bisect
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        sunny_dic = []
        rain_dic = {}

        ans = []

        for i, rain in enumerate(rains):
            if rain > 0:
                # 处理湖里已经有积水的情况，逆转时空，强行排水
                if rain in rain_dic:
                    i1 = rain_dic[rain]  # 上次下雨的日期
                    i2 = bisect.bisect_left(sunny_dic, i1)  # 计算排水的日期（贪心选择更早的日期）

                    # 已经没有时间排水了
                    if i2 == len(sunny_dic):
                        return []

                    i3 = sunny_dic[i2]
                    # print(sunny_dic, i1, "->", i2, "->", i3)

                    # 处理成功排水的情况
                    sunny_dic.pop(i2)
                    ans[i3] = rain
                    del rain_dic[rain]

                rain_dic[rain] = i
                ans.append(-1)
            else:
                sunny_dic.append(i)
                ans.append(1)

            # print(i, ans)

        return ans


if __name__ == "__main__":
    # [-1,-1,-1,-1]
    print(Solution().avoidFlood(rains=[1, 2, 3, 4]))

    # [-1,-1,2,1,-1,-1]
    print(Solution().avoidFlood(rains=[1, 2, 0, 0, 2, 1]))

    # []
    print(Solution().avoidFlood(rains=[1, 2, 0, 1, 2]))

    # [-1,69,1,1,-1]
    print(Solution().avoidFlood(rains=[69, 0, 0, 0, 69]))

    # []
    print(Solution().avoidFlood(rains=[10, 20, 20]))
