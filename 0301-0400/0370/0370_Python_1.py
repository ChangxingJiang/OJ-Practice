from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        lst = [0] * (length + 1)
        for update in updates:
            lst[update[0]] += update[2]
            lst[update[1] + 1] -= update[2]

        ans = []

        now = 0
        for i in range(length + 1):
            now += lst[i]
            ans.append(now)

        return ans[:-1]


if __name__ == "__main__":
    # [-2,0,3,5,3]
    print(Solution().getModifiedArray(length=5, updates=[[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
