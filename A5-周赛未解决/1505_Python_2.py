# O(N^2)
# 数组
# 超出时间限制

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        size = len(num)

        nums = [int(n) for n in num]

        # 排序列表作为参考
        # O(NlogN)
        template = list(sorted(nums))

        # print("模板值:", template)

        # 不断交换位置已变小
        # O(N^2)
        now_idx = 0  # 正在准备变为最小的位数
        aim_to_template = True  # 当前是否再向模板调整
        while k > 0 and now_idx < size:

            # print(nums, k, "-", "NOW:", now_idx, "(", template[now_idx], ")")

            # 处于向模板调整的情况

            if aim_to_template:

                # 计算当前位置是否为模板值
                if nums[now_idx] == template[now_idx]:
                    now_idx += 1
                    continue

                # 寻找距离最近的模板值
                aim_idx = nums.index(template[now_idx], now_idx)

                # 如果在步数范围内找到的当前模板值
                if aim_idx - now_idx <= k:
                    # print("在步数范围内找到当前模板值:", aim_idx, "(步数:", aim_idx - now_idx, ")")
                    nums = nums[:now_idx] + [template[now_idx]] + nums[now_idx:aim_idx] + nums[aim_idx + 1:]
                    k -= (aim_idx - now_idx)
                    now_idx += 1
                    continue

                # 如果在步数范围内没有找到当前模板值
                else:
                    aim_to_template = False

                    # 在当前步数范围内寻找最小值
                    min_idx, min_val = now_idx, nums[now_idx]
                    for i in range(k + 1):
                        if nums[now_idx + i] < min_val:
                            min_idx, min_val = now_idx + i, nums[now_idx + i]

                    # 处理当前值不是步数范围内最小值的情况
                    if min_idx != now_idx:
                        # print("在步数范围内找到了最小值:", min_val, "(", min_idx, ")")
                        nums = nums[:now_idx] + [min_val] + nums[now_idx:min_idx] + nums[min_idx + 1:]
                        k -= min_idx - now_idx

                now_idx += 1

            else:
                # 在当前步数范围内寻找最小值
                min_idx, min_val = now_idx, nums[now_idx]
                for i in range(k + 1):
                    if nums[now_idx + i] < min_val:
                        min_idx, min_val = now_idx + i, nums[now_idx + i]

                # 处理当前值不是步数范围内最小值的情况
                if min_idx != now_idx:
                    # print("在步数范围内找到了最小值:", min_val, "(", min_idx, ")")
                    nums = nums[:now_idx] + [min_val] + nums[now_idx:min_idx] + nums[min_idx + 1:]
                    k -= min_idx - now_idx

                now_idx += 1

        return "".join([str(num) for num in nums])


if __name__ == "__main__":
    print(Solution().minInteger(num="4321", k=4))  # 1342
    print(Solution().minInteger(num="100", k=1))  # 010
    print(Solution().minInteger(num="36789", k=1000))  # 36789
    print(Solution().minInteger(num="22", k=22))  # 22
    print(Solution().minInteger(num="9438957234785635408", k=23))  # 0345989723478563548
    print(Solution().minInteger(num="9000900", k=3))  # 0009900
    print(Solution().minInteger(num="294984148179", k=11))  # 0009900
