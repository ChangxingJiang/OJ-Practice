class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().patternMatching(pattern="abba", value="dogcatcatdog"))  # True
    print(Solution().patternMatching(pattern="abba", value="dogcatcatfish"))  # False
    print(Solution().patternMatching(pattern="aaaa", value="dogcatcatdog"))  # False
    print(Solution().patternMatching(pattern="abba", value="dogdogdogdog"))  # True
