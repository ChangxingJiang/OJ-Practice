from typing import List


class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # 将IP转换为数值
        start = 0
        for x in ip.split("."):
            start = start * 256 + int(x)

        ans = []

        while n > 0:
            mask = min((start & -start), n).bit_length()
            if mask == 0:
                mask += 1
            ans.append(".".join(str((start >> i) % 256) for i in (24, 16, 8, 0)) + "/" + str(33 - mask))
            start += 1 << (mask - 1)
            n -= 1 << (mask - 1)

        return ans


if __name__ == "__main__":
    # ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
    print(Solution().ipToCIDR(ip="255.0.0.7", n=10))

    # ['0.0.0.0/32']
    print(Solution().ipToCIDR(ip="0.0.0.0", n=1))
