from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [1]
        i1, i2 = 2, k + 1
        for i in range(1, k + 1):
            if i % 2 == 1:
                ans.append(i2)
                i2 -= 1
            else:
                ans.append(i1)
                i1 += 1
        ans += [i for i in range(k + 2, n + 1)]
        return ans


if __name__ == "__main__":
    print(Solution().constructArray(3, 1))  # [1,2,3]
    print(Solution().constructArray(3, 2))  # [1,3,2]
    print(Solution().constructArray(5, 2))  # [1,3,2,4,5]
