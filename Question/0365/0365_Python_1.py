import collections


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        ans = set()
        visited = {(0, 0)}
        queue = collections.deque([(0, 0)])
        while queue:
            x1, y1 = queue.popleft()

            ans.add(x1)
            ans.add(y1)
            ans.add(x1 + y1)

            # 将左侧倒满
            x2, y2 = x, y1
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将右侧倒满
            x2, y2 = x1, y
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将左侧倒空
            x2, y2 = 0, y1
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将右侧倒空
            x2, y2 = x1, 0
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将左侧倒到右侧
            t = min(y - y1, x1)
            x2, y2 = x1 - t, y1 + t
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将右侧倒到左侧
            t = min(x - x1, y1)
            x2, y2 = x1 + t, y1 - t
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

        return z in ans


if __name__ == "__main__":
    print(Solution().canMeasureWater(3, 5, 4))  # True
    print(Solution().canMeasureWater(2, 6, 5))  # False
    print(Solution().canMeasureWater(1, 2, 3))  # True
    print(Solution().canMeasureWater(22003, 31237, 1))  # True
