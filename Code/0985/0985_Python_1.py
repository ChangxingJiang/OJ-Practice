from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        total = sum([a for a in A if a % 2 == 0])
        ans = []
        for query in queries:
            a = A[query[1]]
            b = a + query[0]
            A[query[1]] = b
            if a % 2 == 0:
                total -= a
            if b % 2 == 0:
                total += b
            ans.append(total)

        return ans


if __name__ == "__main__":
    print(Solution().sumEvenAfterQueries(A=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]))  # [8,6,2,4]
