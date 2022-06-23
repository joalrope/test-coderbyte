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

def get_median(arr):
    arr.sort()

    nums_len = len(arr)
    half = int(nums_len / 2)

    if nums_len % 2 == 0:
        return (arr[half - 1] + arr[half]) / 2
    return arr[half]


def ArrayChallenge(arr):

    arr = arr.replace('[', '')
    arr = arr.replace(']', '')
    arr = arr.replace(' ', '')

    array = list(map(int, arr.split(',')))

    N = array[0]
    nums = array[1:]

    return get_median(nums)


# keep this function call here
print(ArrayChallenge(
    input('input a list, example [5, 7, 9, 1, 0, 3] ==> :  ')))
