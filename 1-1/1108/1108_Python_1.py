class Solution:
    def defangIPaddr(self, address: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().defangIPaddr(address="1.1.1.1"))  # "1[.]1[.]1[.]1"
    print(Solution().defangIPaddr(address="255.100.50.0"))  # "255[.]100[.]50[.]0"
