class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1, a2 = a[:-1].split("+")
        b1, b2 = b[:-1].split("+")
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        c1 = a1 * b1 - a2 * b2
        c2 = a1 * b2 + a2 * b1
        return str(c1) + "+" + str(c2) + "i"


if __name__ == "__main__":
    print(Solution().complexNumberMultiply("1+1i", "1+1i"))  # "0+2i"
    print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))  # "0+-2i"
