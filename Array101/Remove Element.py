# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.

def removeElement(nums, val):
    count = 0
    #判斷nums 是否為空
    if nums == None or len(nums) == 0:
        return 0;
    else:

        for i in range(len(nums)):
            #判斷是否為符合刪除值
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        print(nums)
        return count

if __name__ == '__main__':
    nums_list = [3, 2, 2, 3]
    val = 3
    removeElement(nums_list, val)
