class Solution:
    def divisorGame(self, N: int) -> bool:
        situations = {
            1: False
        }
        for i in range(2, N + 1):
            chooses = {i - 1}
            for k in (2, i // 2 + 1):
                if i % k == 0 and 0 < i - k < i:
                    chooses.add(i - k)
            situations[i] = not all(situations[choose] for choose in chooses)

        return situations[N]


if __name__ == "__main__":
    print(Solution().divisorGame(2))  # True
    print(Solution().divisorGame(3))  # False
    print(Solution().divisorGame(20))  # True
