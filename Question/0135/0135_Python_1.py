from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)

        ans = 0

        now_orient, num, lst = 0, 1, []  # 当前方向、当前方向数量、当前段各部分数量
        for i in range(1, size):
            # 计算下一个方向
            if ratings[i] - ratings[i - 1] > 0:
                next_orient = 1
            elif ratings[i] - ratings[i - 1] < 0:
                next_orient = -1
            else:
                next_orient = 0

            # 处理两个相邻值相同的情况
            if next_orient == 0:
                lst.append(now_orient * num if now_orient != 0 else 1)

                # 计算当前段的值
                val = 0
                for j in range(len(lst) - 1):
                    if lst[j] < 0 and lst[j + 1] > 0:
                        val -= 1
                    else:
                        val -= min(lst[j], -lst[j + 1])
                for n in lst:
                    val += abs(n) * (abs(n) + 1) // 2

                ans += val

                now_orient, num, lst = 0, 1, []

            # 处理当前方向为相等的情况
            elif now_orient == 0:
                num += 1
                now_orient = next_orient

            # 处理方向没有变化的情况
            elif next_orient == now_orient:
                num += 1

            # 处理当期方向不同的情况
            else:
                lst.append(now_orient * num if now_orient != 0 else 1)

                now_orient = next_orient
                num = 2

        else:
            lst.append(now_orient * num if now_orient != 0 else 1)

            # 计算当前段的值
            val = 0
            for j in range(len(lst) - 1):
                if lst[j] < 0 and lst[j + 1] > 0:
                    val -= 1
                else:
                    val -= min(lst[j], -lst[j + 1])
            for n in lst:
                val += abs(n) * (abs(n) + 1) // 2

            ans += val

        return ans


if __name__ == "__main__":
    print(Solution().candy([1, 0, 2]))  # 5
    print(Solution().candy([1, 2, 2]))  # 4
    print(Solution().candy([2, 2, 1]))  # 4
    print(Solution().candy([1, 3, 4, 5, 2]))  # 11
    print(Solution().candy([1, 6, 10, 8, 7, 3, 2]))  # 18
