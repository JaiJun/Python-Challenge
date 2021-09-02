# Given integer array nums, return the third maximum number in this array.
# If the third maximum does not exist, return the maximum number.

def thirdMax(nums):
    if len(nums) < 3:
        return max(nums)
    else:
        max_number = max(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] <= max_number:
                max_number = nums[i]
                count += 1
            else:
                count += 1
        print(max_number)
        return max_number


if __name__ == '__main__':
    nums = [1, 2]
    # nums = [5, 3, 2, 1]
    print(thirdMax(nums))
