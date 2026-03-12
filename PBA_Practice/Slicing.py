# ======================== NUMPY SLICING - THEORY ========================
#
# Slicing syntax in NumPy/Python:
# array[start : stop : step]
#
# Important points:
# 1) start index is included.
# 2) stop index is excluded.
# 3) step controls jump between elements.
# 4) Negative step can reverse an array.
#
# =======================================================================

import numpy as np


# Given array from the question
arr = np.array([10, 20, 30, 40, 50, 60, 70])


# 1) Print elements from index 1 to 3
# index 1 to 3 means include index 1,2,3 -> use stop as 4
slice_1_to_3 = arr[1:4]   # Output: [20 30 40]


# 2) Print every second element
# start at index 1 so output matches notes like [20 40 60]
every_second = arr[1::2]  # Output: [20 40 60]


# 3) Reverse the array
# step -1 means move from end to start
reversed_array = arr[::-1]  # Output: [70 60 50 40 30 20 10]


# 4) Print elements from index 2 to 5
# include indices 2,3,4,5 -> use stop as 6
slice_2_to_5 = arr[2:6]   # Output: [30 40 50 60]


# 5) Print elements using negative slicing
# From second last element to index 1 (in reverse direction)
# This gives output style often seen in notes for negative slicing.
negative_slice = arr[-2:0:-1]  # Output: [60 50 40 30 20]


# ======================== OUTPUT SECTION ========================
if __name__ == "__main__":
	print("Given Array:", arr)
	print()

	print("1) Elements from index 1 to 3 (arr[1:4]):", slice_1_to_3)
	print("2) Every second element (arr[1::2]):", every_second)
	print("3) Reverse the array (arr[::-1]):", reversed_array)
	print("4) Elements from index 2 to 5 (arr[2:6]):", slice_2_to_5)
	print("5) Negative slicing (arr[-2:0:-1]):", negative_slice)
