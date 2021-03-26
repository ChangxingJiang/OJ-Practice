import bisect
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        size1, size2 = len(mat), len(mat[0])

        hashmap = {i: 0 for i in range(size1)}
        now = [m[0] for m in mat]

        while len(set(now)) > 1:

            max_val = max(now)

            for i in range(size1):
                idx = bisect.bisect(mat[i], max_val, lo=hashmap[i])
                # print(mat[i], max_val, "->", idx - 1)
                if mat[i][idx - 1] == max_val:
                    hashmap[i] = idx - 1
                elif idx >= size2:
                    return -1
                else:
                    hashmap[i] = idx

            now = [mat[i][hashmap[i]] for i in range(size1)]

        return now[0]


if __name__ == "__main__":
    # 5
    print(Solution().smallestCommonElement(mat=[[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
