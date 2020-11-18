from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        prefix = [1]
        now = 1
        for n in a:
            now *= n
            prefix.append(now)

        suffix = [1]
        now = 1
        for n in a[::-1]:
            now *= n
            suffix.append(now)
        suffix.reverse()

        ans = []
        for i in range(len(a)):
            ans.append(prefix[i] * suffix[i + 1])

        return ans


if __name__ == "__main__":
    print(Solution().constructArr([1, 2, 3, 4, 5]))  # [120,60,40,30,24]
