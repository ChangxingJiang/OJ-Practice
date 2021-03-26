import collections
import heapq
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # 统计学生得分
        count = collections.defaultdict(list)
        for student, mark in items:
            heapq.heappush(count[student], mark)
            if len(count[student]) > 5:
                heapq.heappop(count[student])

        # 计算学生平均分
        ans = [[student, sum(lst) // 5] for student, lst in count.items()]
        ans.sort(key=lambda x: x[0])

        return ans


if __name__ == "__main__":
    # [[1,87],[2,88]]
    print(Solution().highFive(
        items=[[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))

    # [[1,100],[7,100]]
    print(Solution().highFive(
        items=[[1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100]]))
