from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)

        prefix = []  # 将前面的小球全部移动到当前位置
        last = now = 0
        for i in range(size):
            last += now
            prefix.append(last)
            if boxes[i] == "1":
                now += 1

        suffix = []  # 将后面的小球全部移动到当前位置
        last = now = 0
        for i in range(size - 1, -1, -1):
            last += now
            suffix.append(last)
            if boxes[i] == "1":
                now += 1
        suffix.reverse()

        return [prefix[i] + suffix[i] for i in range(size)]


if __name__ == "__main__":
    print(Solution().minOperations("110"))  # [1,1,3]
    print(Solution().minOperations("001011"))  # [11,8,5,4,3,4]
