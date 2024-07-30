def merge(nums1, m, nums2, n) -> None:
    """
    Merges two sorted arrays nums1 and nums2. 
    The first m elements of nums1 are valid, and the first n elements of nums2 are valid.
    The merged result should be in nums1 in-place.
    """
    
    # Last index of nums1 (considering it has enough space to hold nums2)
    last = m + n - 1
    print(last,"last")
    
    # Pointers for nums1 and nums2
    i = m - 1
    j = n - 1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            print(nums1[i], nums2[j])
            nums1[last] = nums1[i]
            print(nums1[last],"in if", nums1)
            i -= 1
        else:
            nums1[last] = nums2[j]
            print(nums1[i], nums2[j])
            print(nums1[last], "in else", nums1)
            j -= 1
        last -= 1

    # Fill nums1 with remaining elements of nums2 (if any)
    while j >= 0:
        nums1[last] = nums2[j]
        print("2nd while")
        j -= 1
        last -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]