class Solution:
    def validIPAddress(self, IP: str) -> str:
        # 尝试识别IPv4的IP地址
        lst4 = IP.split(".")
        if len(lst4) == 4:
            for item in lst4:
                if not item.isdigit() or int(item) > 255 or (int(item) != 0 and item[0] == "0") or (int(item) == 0 and len(item) > 1):
                    break
            else:
                return "IPv4"

        # 尝试识别IPv6的IP地址
        chars = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
        lst6 = IP.upper().split(":")
        if len(lst6) == 8:
            for item in lst6:
                if len(item) == 0 or len(item) > 4 or not all([ch in chars for ch in item]):
                    break
            else:
                return "IPv6"

        return "Neither"


if __name__ == "__main__":
    print(Solution().validIPAddress("172.16.254.1"))  # "IPv4"
    print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))  # "IPv6"
    print(Solution().validIPAddress("256.256.256.256"))  # "Neither"
    print(Solution().validIPAddress("1e1.4.5.6"))  # "Neither"
    print(Solution().validIPAddress("00.0.0.0"))  # "Neither"
    print(Solution().validIPAddress("2001:0db8:85a3:00000:0:8A2E:0370:7334"))  # "Neither"
    print(Solution().validIPAddress("2001:0db8:85h3:0000:0:8A2E:0370:7334"))  # "Neither"
    print(Solution().validIPAddress("20EE:Fb8:85a3:0:0:8A2E:0370:7334"))  # "IPv6"
    print(Solution().validIPAddress("2001:db8:85a3:0::8a2E:0370:7334"))  # "Neither"
