# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


def moveZeroes(nums):
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] == 0 :
            j +=1
        else:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i +=1
            j +=1
    return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)