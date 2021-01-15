class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n1 = binary.count("0")
        if n1 <= 1:
            return binary

        n2 = 0
        for c in binary:
            if c != "1":
                break
            n2 += 1

        n3 = len(binary)

        return "1" * (n2 + n1 - 1) + "0" + "1" * (n3 - n2 - n1)


if __name__ == "__main__":
    print(Solution().maximumBinaryString(binary="000110"))  # "111011"
    print(Solution().maximumBinaryString(binary="01"))  # "01"
    print(Solution().maximumBinaryString(binary="11"))  # "11"
    print(Solution().maximumBinaryString(binary="1100"))  # "1110"
