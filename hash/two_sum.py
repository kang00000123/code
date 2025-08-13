def two_sum(nums, target):
    """
    找到数组中两个数的和等于目标值，返回它们的索引
    """
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []


# 测试用例
if __name__ == "__main__":
    # 示例1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {two_sum(nums1, target1)}")  # [0, 1]

    # 示例2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"输入: nums = {nums2}, target = {target2}")
    print(f"输出: {two_sum(nums2, target2)}")  # [1, 2]

    # 示例3
    nums3 = [3, 3]
    target3 = 6
    print(f"输入: nums = {nums3}, target = {target3}")
    print(f"输出: {two_sum(nums3, target3)}")  # [0, 1]
