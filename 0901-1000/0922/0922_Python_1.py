from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        type1 = []
        type2 = []
        for i in range(len(A)):
            i2 = i % 2
            A2 = A[i] % 2
            if i2 != A2:
                if i2 == 0:
                    if len(type1) > 0:
                        n = type1.pop()
                        A[n], A[i] = A[i], A[n]
                    else:
                        type2.append(i)
                else:
                    if len(type2) > 0:
                        n = type2.pop()
                        A[n], A[i] = A[i], A[n]
                    else:
                        type1.append(i)

        return A


if __name__ == "__main__":
    print(Solution().sortArrayByParityII([4, 2, 5, 7]))  # [4,5,2,7]
    print(Solution().sortArrayByParityII([3, 4]))  # [4,3]
    print(Solution().sortArrayByParityII(
        [648, 831, 560, 986, 192, 424, 997, 829, 897, 843]))  # [648,831,560,997,192,897,986,829,424,843]
