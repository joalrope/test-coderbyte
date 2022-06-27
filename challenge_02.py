# Array Challenge
# Have the function ArrayChallenge(arr) read the array of
# numbers stored in arr which will contain a sliding window size, N,
# as the first element in the array and the rest will be a list of numbers.
# Your program should return the Moving Median for each element based
# on the element and its N-1 predecessors, where N is the sliding window size.
# The final output should be a string with the moving median corresponding
# to each entry in the original array separated by commas.

# Note that for the first few elements (until the window size is reached),
# the median is computed on a smaller number of entries.
# For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1]
# then your program should output "1,2,3,5,6,6,4,3"
#
# Examples
# Input: [5, 2, 4, 6]
# Output: 2,3,4
# Input: [3, 0, 0, -2, 0, 2, 0, -2]
# Output: 0,0,0,0,0,0,0

from typing import List


def get_median(arr: List[int]) -> int:
    arr.sort()

    length = len(arr)

    if (length == 1):
        return arr[0]
    elif (length == 2):
        return (arr[0]+arr[1])/2
    elif (length == 3):
        return arr[1]
    else:
        if not length % 2:
            print('N par')
            a = arr[int(length/2)]
            b = arr[int((length/2)-1)]
            new_arr = [a, b]
            return get_median(new_arr)
        else:
            print('N impar')
            return arr[int(length/2)]


def ArrayChallenge(arr: List[int]):

    arr = arr.replace('[', '')
    arr = arr.replace(']', '')
    arr = arr.replace(' ', '')

    array = list(map(int, arr.split(',')))

    N = array[0]
    nums = array[1:]
    result = ''

    for k in range(0, len(nums)):
        if (k < N):
            if k == 0:
                result = str(get_median(nums[0: k+1]))
            else:
                result = result + ',' + str(get_median(nums[0: k+1]))
        else:
            result = result + ',' + str(get_median(nums[k+1-N: k+1]))

    return result


# keep this function call here
print(ArrayChallenge(
    input('input a list, example [5, 2, 4, 6] ==> :  ')))
