from typing import List

def removeElement(nums: List[int], val: int) -> int:


    """
    Given an integer array nums and an integer val, 
    remove all occurrences of val in nums in-place. 
    The order of the elements may be changed. 
    Then return the number of elements in nums which are not equal to val.
    """

    # Pointer for the place to insert the next valid element
    insert_pos = 0
    
    # Iterate over each element in the array
    for i in range(len(nums)):
        # If the current element is not equal to val, move it to the insert position
        if nums[i] != val:
            nums[insert_pos] = nums[i]
            insert_pos += 1
    
    # insert_pos is now the length of the array without the val elements
    return insert_pos

# Example usage:
nums = [3, 2, 2, 3, 4, 2, 3]
val = 3
length = removeElement(nums, val)
print(f"Array after removal: {nums[:length]}, Length: {length}")
