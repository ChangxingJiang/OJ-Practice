# O(N^2)
# 超出时间限制

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        size = len(num)

        nums = [int(n) for n in num]

        # 排序列表作为参考
        # O(NlogN)
        template = list(sorted(nums))

        # 不断交换位置已变小
        # O(N^2)
        now = 0  # 正在准备变为最小的位数
        while now < size:

            # print(nums, k, "-", "NOW:", now)

            # 计算当前位置是否为模板值
            if nums[now] == template[now]:
                now += 1
                continue

            # 寻找距离最近的模板值
            min_idx, min_val = now, nums[now]
            step = 1
            while step <= k and now + step < size:
                # 如果在步数范围内找到的当前模板值
                if nums[now + step] == template[now]:
                    nums = nums[:now] + [template[now]] + nums[now:now + step] + nums[now + step + 1:]
                    k -= step
                    break

                # 寻找当前步数范围内的最小值
                if nums[now + step] < min_val:
                    min_idx, min_val = now + step, nums[now + step]

                step += 1

            # 处理找到模板值的情况
            if nums[now] == template[now]:
                now += 1
                continue

            # 处理没有找到模板值的情况
            else:
                # 处理当前值不是步数范围内最小值的情况
                if min_idx != now:
                    nums = nums[:now] + [min_val] + nums[now:min_idx] + nums[min_idx + 1:]
                    k -= min_idx - now

                # 处理当前值就是步数范围内最小值的情况
                else:
                    pass

            now += 1

        return "".join([str(num) for num in nums])


if __name__ == "__main__":
    print(Solution().minInteger(num="4321", k=4))  # 1342
    print(Solution().minInteger(num="100", k=1))  # 010
    print(Solution().minInteger(num="36789", k=1000))  # 36789
    print(Solution().minInteger(num="22", k=22))  # 22
    print(Solution().minInteger(num="9438957234785635408", k=23))  # 0345989723478563548
