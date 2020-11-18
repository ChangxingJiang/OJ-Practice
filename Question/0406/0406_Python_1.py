from collections import defaultdict
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 以高度整理数据
        # 时间:O(N) 空间:O(N)
        count = defaultdict(list)
        for h, k in people:
            count[h].append(k)

        size = len(people)

        # 贪心算法：从小到大考虑填写
        ans = [[-1, -1]] * size
        for h in sorted(count.keys()):
            k_list = list(sorted(count[h]))

            j, now = 0, -1
            for i in range(size):
                if ans[i] == [-1, -1]:
                    now += 1
                    if now == k_list[j]:
                        ans[i] = [h, k_list[j]]
                        j += 1
                        if j == len(k_list):
                            break
            # print(ans)

        return ans


if __name__ == "__main__":
    # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

    # [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]
    print(Solution().reconstructQueue([[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]))
