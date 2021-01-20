from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = []
        for i in range(1 << n):
            ans.append(i ^ (i >> 1) ^ start)  # 新各类编码为标准各类编码异或start
        return ans


if __name__ == "__main__":
    print(Solution().circularPermutation(n=2, start=3))  # [3,2,0,1]
    print(Solution().circularPermutation(n=3, start=2))  # [2,6,7,5,4,0,1,3]
