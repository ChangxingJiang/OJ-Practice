from typing import List


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        ans1, ans2 = 0, 0


        colors = ["R", "Y", "G", "B"]
        lst1 = [0, 0, 0, 0]
        lst2 = [0, 0, 0, 0]
        for i in range(4):
            if solution[i] == guess[i]:
                ans1 += 1
            else:
                lst1[colors.index(solution[i])] += 1
                lst2[colors.index(guess[i])] += 1

        for i in range(4):
            ans2 += min(lst1[i], lst2[i])

        return [ans1, ans2]


if __name__ == "__main__":
    print(Solution().masterMind(solution="RGBY", guess="GGRR"))  # [1,1]
