from typing import List


def removeDuplicates(nums: List[int]) -> int:

    #Remove Duplicates from sorted Array 2

    """
    Given an integer array nums sorted in non-decreasing order, 
    remove some duplicates in-place such that each unique element appears at most twice. 
    The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, 
    you must instead have the result be placed in the first part of the array nums. 
    More formally, if there are k elements after removing the duplicates, 
    then the first k elements of nums should hold the final result. 
    It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. 
    You must do this by modifying the input array in-place with O(1) extra memory.
    """

    if len(nums) <= 2:
        return len(nums)

    write_index = 1  # Start writing from the second element
    count = 1  # Start count from the second element

    for read_index in range(1, len(nums)):
        if nums[read_index] == nums[read_index - 1]:
            count += 1
        else:
            count = 1  # Reset count for a new element

        if count <= 2:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index

# Example usage:

nums = [1, 1, 1, 2, 2, 3]
k = removeDuplicates(nums)
print(f"Array after removal: {nums[:k]}, Length: {k}")
    