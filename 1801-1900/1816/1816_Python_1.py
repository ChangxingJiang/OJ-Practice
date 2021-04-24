class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])


if __name__ == "__main__":
    print(Solution().truncateSentence(s="Hello how are you Contestant", k=4))
    print(Solution().truncateSentence(s="What is the solution to this problem", k=4))
    print(Solution().truncateSentence(s="chopper is not a tanuki", k=5))
