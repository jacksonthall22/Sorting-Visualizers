import random

INDENT = '----'


def mergeSortDebug(nums, start, stop, depth):
    if depth == 0:
        print('----Starting Merge Sort')
        print(f'----nums: {nums}')

    print(f'\n' + (INDENT * depth) + '----Current range in nums: ' +
            ' | '.join([[' ', str(e)][i in range(start, stop)] 
            for i, e in enumerate(nums)]))
    print((INDENT * depth) + f'----Start and Stop: [{start}, {stop})')
    middle = (start + stop) // 2

    # Shouldn't be called where start = stop
    assert start != stop

    if start == stop - 1:
        print((INDENT * depth) + '----start == stop - 1, returning')
        print((INDENT * depth) + f'----nums: {nums}')
        return
    elif start == stop - 2:
        print((INDENT * depth) + '----start == stop - 2')
        # Put two elements in order
        if nums[start] > nums[stop - 1]:
            print((INDENT * depth) + '----swapping 2 consecutive elements')
            nums[start], nums[stop - 1] = nums[stop - 1], nums[start]
        else:
            print((INDENT * depth) + '----elements in order, returning')
    else:
        print((INDENT * depth) + '----mergeSort() and merge 2 halves')
        # Merge two halves
        mergeSortDebug(nums, start, middle, depth + 1)
        mergeSortDebug(nums, middle, stop, depth + 1)

        # Current index to start sorting
        firstHalfIndex = start
        secondHalfIndex = middle

        print((INDENT * depth) + '----Merging:')
        for _ in range(start, stop):
            print(' | '.join(
                    [{'00': ' ', '01': 's', '10': 'x', '11': 'B'}[
                    str(int(i == firstHalfIndex or i == secondHalfIndex))
                    + str(int(i == start or i == stop - 1))]
                    for i, e in enumerate(nums)]))
            print(' | '.join([[' ', str(e)][i in range(start, stop)]
                              for i, e in enumerate(nums)]))

            if nums[secondHalfIndex] < nums[firstHalfIndex]:
                nums.insert(firstHalfIndex, nums.pop(secondHalfIndex))
                firstHalfIndex += 1
                secondHalfIndex += 1
            else:
                firstHalfIndex += 1

            # First partition runs out or second partition runs out
            if firstHalfIndex == secondHalfIndex \
                    or secondHalfIndex == stop:
                print(' | '.join([{'00': ' ', '01': 's', '10': 'x', '11': 'B'}[
                        str(int(i == firstHalfIndex or i == secondHalfIndex))
                        + str(int(i == start or i == stop - 1))]
                        for i, e in enumerate(nums)]))
                print(' | '.join([[' ', str(e)][i in range(start, stop)]
                                  for i, e in enumerate(nums)]))
                print((INDENT * depth) + '----End condition reached for merge')
                break

    print((INDENT * depth) + f'----nums: {nums}')
    print()


def mergeSort(nums, start, stop):
    middle = (start + stop) // 2

    if start == stop - 1:
        return
    elif start == stop - 2:
        # Put two elements in order
        if nums[start] > nums[stop - 1]:
            nums[start], nums[stop - 1] = nums[stop - 1], nums[start]
    else:
        # Merge two halves
        mergeSort(nums, start, middle)
        mergeSort(nums, middle, stop)

        # Index of element in first and second halves to compare while merging
        firstHalfIndex = start
        secondHalfIndex = middle

        # While numbers in the first and second partition haven't run out
        while firstHalfIndex != secondHalfIndex and secondHalfIndex != stop:
            # Iff first number in the second partition is bigger than
            # first number in the first, swap them
            if nums[secondHalfIndex] < nums[firstHalfIndex]:
                nums.insert(firstHalfIndex, nums.pop(secondHalfIndex))
                firstHalfIndex += 1
                secondHalfIndex += 1
            else:
                firstHalfIndex += 1


def histogramize(lst):
    # Keep lst short for now
    assert len(lst) <= 30 and max(lst) < 30

    for lineNum in range(max(lst), 0, -1):
        for charNum in range(len(lst)):
            if lst[charNum] >= lineNum:
                print('*', end=' ')
            else:
                print(' ', end=' ')

        print()



def main():
    # nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # nums = [2, 6, 7, 9, 11, 0, 1, 3, 4, 10, 12]
    nums = list(range(1, 11))

    n = 100000
    print(f'Merge Sorting {n} times...', end='')

    for i in range(n):
        random.shuffle(nums)
        mergeSort(nums, 0, len(nums))
        assert nums == sorted(nums)

    print(' done! No failed assertions.')


if __name__ == '__main__':
    main()
