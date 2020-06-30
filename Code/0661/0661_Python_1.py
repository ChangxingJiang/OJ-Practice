from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        x = len(M)
        y = len(M[0])
        N = [[-1 for _ in range(y)] for _ in range(x)]
        for i in range(x):
            for j in range(y):
                ans = [M[i][j]]
                if i > 0:
                    ans.append(M[i - 1][j])
                    if j > 0:
                        ans.append(M[i - 1][j - 1])
                    if j < y - 1:
                        ans.append(M[i - 1][j + 1])
                if i < x - 1:
                    ans.append(M[i + 1][j])
                    if j > 0:
                        ans.append(M[i + 1][j - 1])
                    if j < y - 1:
                        ans.append(M[i + 1][j + 1])
                if j > 0:
                    ans.append(M[i][j - 1])
                if j < y - 1:
                    ans.append(M[i][j + 1])
                print(i, j, ans, int(sum(ans) / len(ans)))
                N[i][j] = int(sum(ans) / len(ans))
        return N


if __name__ == "__main__":
    print(Solution().imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    # [[0,0,0],[0,0,0],[0,0,0]]

    print(Solution().imageSmoother([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]))
    # [[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]
