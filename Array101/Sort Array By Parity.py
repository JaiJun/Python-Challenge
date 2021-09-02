# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#
# Return any array that satisfies this condition.

def sortArrayByParity(nums):
    even = []
    odd = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    return even + odd

if __name__ == '__main__':
    nums = [3, 1, 2, 4]
    sortArrayByParity(nums)