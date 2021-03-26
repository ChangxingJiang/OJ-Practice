from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 排序数组
        # 时间:O(NlogN) 空间:O(N)
        people.sort(key=lambda x: (-x[0], x[1]))

        # 从大到小插入
        # 时间:O(N^2) 空间:O(N)
        ans = []
        for p in people:
            ans.insert(p[1], p)

        return ans


if __name__ == "__main__":
    # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

    # [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]
    print(Solution().reconstructQueue([[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]))
