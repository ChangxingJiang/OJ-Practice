from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        for n in range(2, int((target * 2) ** 0.5 + 1)):
            a, b = divmod(target, n)
            c, d = divmod(int(n * (n - 1) / 2), n)
            if b == d:
                ans.append([a - c + i for i in range(n)])
        return ans[::-1]


if __name__ == "__main__":
    # [[2,3,4],[4,5]]
    print(Solution().findContinuousSequence(9))

    # [[1,2,3,4,5],[4,5,6],[7,8]]
    print(Solution().findContinuousSequence(15))
