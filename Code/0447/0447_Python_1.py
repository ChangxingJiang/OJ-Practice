from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p1 in points:
            hashmap = {}
            for p2 in points:
                s = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                if s in hashmap:
                    hashmap[s] += 1
                else:
                    hashmap[s] = 1

            for key, value in hashmap.items():
                if key != 0:
                    ans += value * (value - 1)

        return ans


if __name__ == "__main__":
    print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))  # 2
    print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]))  # 20
