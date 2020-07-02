from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        idx = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 != 0:
                while A[idx] % 2 != 0:
                    idx += 2
                A[idx], A[i] = A[i], A[idx]
        return A


if __name__ == "__main__":
    print(Solution().sortArrayByParityII([4, 2, 5, 7]))  # [4,5,2,7]
    print(Solution().sortArrayByParityII([3, 4]))  # [4,3]
    print(Solution().sortArrayByParityII(
        [648, 831, 560, 986, 192, 424, 997, 829, 897, 843]))  # [648,831,560,997,192,897,986,829,424,843]
