# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order by height.
# Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
# You are given an integer array heights representing the current order that the students are standing in.
# Each heights[i] is the height of the ith student in line (0-indexed).
# Return the number of indices where heights[i] != expected[i].

def heightChecker(arr):
    sort_arr = sorted(arr)
    count = 0
    for i in range(len(arr)):
        if arr[i] != sort_arr[i]:
            count += 1
    return count
    # return sum(a != b for a, b in zip(sorted(heights), heights))

if __name__ == '__main__':
    heights = [1, 1, 4, 2, 1, 3]
    heightChecker(heights)
