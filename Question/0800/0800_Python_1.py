class Solution:
    def similarRGB(self, color: str) -> str:
        lst = [i for i in range(0, 256, 17)]
        r1, g1, b1 = int(color[1:3], base=16), int(color[3:5], base=16), int(color[5:7], base=16)

        r2 = min(lst, key=lambda x: abs(r1 - x))
        g2 = min(lst, key=lambda x: abs(g1 - x))
        b2 = min(lst, key=lambda x: abs(b1 - x))

        return "#" + hex(r2)[2:].zfill(2) + hex(g2)[2:].zfill(2) + hex(b2)[2:].zfill(2)


if __name__ == "__main__":
    print(Solution().similarRGB(color="#09f166"))  # "#11ee66"
