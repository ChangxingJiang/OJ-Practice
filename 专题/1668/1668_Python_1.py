class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxRepeating(sequence="ababc", word="ab"))  # 2
    print(Solution().maxRepeating(sequence="ababc", word="ba"))  # 1
    print(Solution().maxRepeating(sequence="ababc", word="ac"))  # 0
