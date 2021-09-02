# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

def R_D_f_S_A(nums):
    if nums == None or len(nums) == 0:
        return 0
    else:
        i,j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
            j+=1
        print(nums)
        return i + 1
if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    R_D_f_S_A(nums)