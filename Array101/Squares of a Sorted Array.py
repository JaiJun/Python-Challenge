# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def squares(list_number):
    squares_number = []
    for number in list_number:
        n = number * number
        squares_number.append(n)
    return sorted(squares_number)

if __name__ == '__main__':
    list_number = [-4,-1,0,3,10]
    squares(list_number)