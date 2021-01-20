from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people_list = [[] for _ in range(max(groupSizes) + 1)]

        for i, n in enumerate(groupSizes):
            people_list[n].append(i)

        groups = []
        for i in range(1, len(people_list)):
            for j in range(0, len(people_list[i]), i):
                groups.append(people_list[i][j:j + i])
        return groups


if __name__ == "__main__":
    # [[5],[0,1,2],[3,4,6]]
    print(Solution().groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))

    # [[1],[0,5],[2,3,4]]
    print(Solution().groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]))
