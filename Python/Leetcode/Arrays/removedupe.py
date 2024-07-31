from typing import List

def removeDuplicates(self, nums: List[int]) -> int:

    """
    Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. 
    Then return the number of unique elements in nums.
    """

    #initialize our write pointer at 0
    write_pos = 0

    #iterate thru the nums array with our read pointer
    for read_pos in range(len(nums)):

        #if the read and write pointer are differ, then we have unique elem at read pointer
        if(nums[read_pos] != nums[write_pos]):

            #increment write pounter and copy new unique elem their
            write_pos += 1
            nums[write_pos] = nums[read_pos]

    #return our write pointer + 1
    return write_pos + 1