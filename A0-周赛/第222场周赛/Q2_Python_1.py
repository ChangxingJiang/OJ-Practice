import collections
from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        count = collections.Counter()

        ans = 0

        for d1 in deliciousness:
            # 统计当前美味程度可以带来的结果数
            if d1 in count:
                ans += count[d1]

            # 记录当前美味程度需要的另一个美味程度
            for i in range(22):  # 0+1=1:2的0次幂;两个2的20次方的和是2的21次方(第68个测试用例)
                d2 = 2 ** i - d1
                if d2 >= 0:
                    count[d2] += 1

        return ans % self._MOD


if __name__ == "__main__":
    print(Solution().countPairs(deliciousness=[1, 3, 5, 7, 9]))  # 4
    print(Solution().countPairs(deliciousness=[1, 1, 1, 3, 3, 3, 7]))  # 15

    print(Solution().countPairs(deliciousness=[2, 2, 2, 2, 2]))  # 10
    print(Solution().countPairs(deliciousness=[2]))  # 0
