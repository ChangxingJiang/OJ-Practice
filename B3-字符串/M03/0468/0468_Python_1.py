class Solution:
    def validIPAddress(self, IP: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().validIPAddress("172.16.254.1"))  # "IPv4"
    print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))  # "IPv6"
    print(Solution().validIPAddress("256.256.256.256"))  # "Neither"
