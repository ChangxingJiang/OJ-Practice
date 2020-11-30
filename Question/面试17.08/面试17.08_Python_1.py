from typing import List


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        size = len(height)

        people = [(height[i], weight[i]) for i in range(size)]
        people.sort()

        print(people)

        # 初始化状态表格
        dp1 = [1 for _ in range(size)]
        dp2 = [1 for _ in range(size)]

        # 状态转移计算
        for i in range(1, size):
            h1, w1 = people[i]
            dp2[i] = dp2[i - 1]
            for j in range(i - 1, -1, -1):
                h2, w2 = people[j]
                if h2 < h1 and w2 < w1:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
                    if dp2[j] < dp2[i] - 1:
                        break
            dp2[i] = max(dp2[i], dp1[i])

        # print(dp1)
        # print(dp2)

        return dp2[-1]


if __name__ == "__main__":
    # 6
    print(Solution().bestSeqAtIndex(height=[65, 70, 56, 75, 60, 68],
                                    weight=[100, 150, 90, 190, 95, 110]))

    # 3
    print(Solution().bestSeqAtIndex(height=[8378, 8535, 8998, 3766, 648, 6184, 5506, 5648, 3907, 6773],
                                    weight=[9644, 849, 3232, 3259, 5229, 314, 5593, 9600, 6695, 4340]))

    # 5
    print(Solution().bestSeqAtIndex(height=[65, 70, 56, 75, 60, 68],
                                    weight=[100, 150, 90, 190, 115, 110]))
