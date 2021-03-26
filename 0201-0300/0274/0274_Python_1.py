from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i in range(len(citations)):
            ans = max(ans, min(i + 1, citations[i]))
            if citations[i] <= ans:
                break
        return ans


if __name__ == "__main__":
    print(Solution().hIndex(citations=[3, 0, 6, 1, 5]))  # 3
