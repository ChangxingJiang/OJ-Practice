from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0

        now = 0
        count = {now: [1, -1, 0]}
        for i, n in enumerate(arr):
            now ^= n
            if now in count:
                a, b, c = count[now]  # 出现次数总计，上一次出现的坐标、、总计出现次数
                res = (i - b) * a + c - 1
                ans += res
                count[now] = [a + 1, i, res]
            else:
                count[now] = [1, i, 0]

        return ans


if __name__ == "__main__":
    print(Solution().countTriplets([2, 3, 1, 6, 7]))  # 4
    print(Solution().countTriplets([1, 1, 1, 1, 1]))  # 10
    print(Solution().countTriplets([2, 3]))  # 0
    print(Solution().countTriplets([1, 3, 5, 7, 9]))  # 3
    print(Solution().countTriplets([7, 11, 12, 9, 5, 2, 7, 17, 22]))  # 8
