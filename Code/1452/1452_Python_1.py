from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(favoriteCompany) for favoriteCompany in favoriteCompanies]
        ans = []
        for i, favoriteCompany1 in enumerate(favoriteCompanies):
            for favoriteCompany2 in favoriteCompanies:
                if favoriteCompany1 < favoriteCompany2:
                    break
            else:
                ans.append(i)
        return ans


if __name__ == "__main__":
    # [0,1,4]
    print(Solution().peopleIndexes(
        favoriteCompanies=[
            ["leetcode", "google", "facebook"],
            ["google", "microsoft"],
            ["google", "facebook"],
            ["google"], ["amazon"]
        ]))

    # [0,1]
    print(Solution().peopleIndexes(
        favoriteCompanies=[
            ["leetcode", "google", "facebook"],
            ["leetcode", "amazon"],
            ["facebook", "google"]
        ]))

    # [0,1,2,3]
    print(Solution().peopleIndexes(
        favoriteCompanies=[
            ["leetcode"],
            ["google"],
            ["facebook"],
            ["amazon"]
        ]))
