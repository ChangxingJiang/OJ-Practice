from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # 使用哈希表存储分组关系
        group_dict = {}
        for pair in pairs:
            group_dict[pair[0]] = pair[1]
            group_dict[pair[1]] = pair[0]

        # 使用哈希表存储亲近程度
        preference_dict = {}
        for i in range(n):
            friends = {}
            for j in range(n):
                if j == i:
                    continue
                elif j > i:
                    j -= 1
                friends[preferences[i][j]] = j
            preference_dict[i] = friends

        ans = 0
        for pair in pairs:
            f1, f2 = pair[0], pair[1]
            for ff1 in preferences[f1]:
                if ff1 == f2:  # 处理已经遍历到配对队友的情况
                    break
                elif preference_dict[ff1][f1] < preference_dict[ff1][group_dict[ff1]]:  # 判断更喜欢的朋友是否更喜欢自己
                    ans += 1
                    break
            for ff1 in preferences[f2]:
                if ff1 == f1:  # 处理已经遍历到配对队友的情况
                    break
                elif preference_dict[ff1][f2] < preference_dict[ff1][group_dict[ff1]]:  # 判断更喜欢的朋友是否更喜欢自己
                    ans += 1
                    break

        return ans


if __name__ == "__main__":
    print(Solution().unhappyFriends(n=4, preferences=[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs=[[0, 1], [2, 3]]))  # 2
    print(Solution().unhappyFriends(n=2, preferences=[[1], [0]], pairs=[[1, 0]]))  # 0
    print(Solution().unhappyFriends(n=4, preferences=[[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs=[[1, 3], [0, 2]]))  # 4
