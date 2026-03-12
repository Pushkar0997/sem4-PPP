# ======================== NUMPY ARRAY ATTRIBUTES - THEORY ========================
#
# In NumPy, an array has useful built-in attributes:
# 1) ndim     -> number of dimensions
# 2) shape    -> size of array in each dimension (rows, columns, etc.)
# 3) size     -> total number of elements
# 4) dtype    -> data type of elements
# 5) itemsize -> memory size (in bytes) of one element
#
# ================================================================================

import numpy as np


# Given array in the question
arr = np.array([
	[10, 20, 30],
	[40, 50, 60],
	[70, 80, 90]
])


# 1) Find number of dimensions
number_of_dimensions = arr.ndim

# 2) Find shape of the array
array_shape = arr.shape

# 3) Find total number of elements
total_elements = arr.size

# 4) Find data type of the array
data_type = arr.dtype

# 5) Find item size of each element
element_item_size = arr.itemsize


# ======================== OUTPUT SECTION ========================
if __name__ == "__main__":
	print("Given Array:\n", arr)
	print()

	print("1) Number of dimensions (ndim):", number_of_dimensions)
	print("2) Shape of array (shape):", array_shape)
	print("3) Total number of elements (size):", total_elements)
	print("4) Data type of elements (dtype):", data_type)
	print("5) Item size of each element (itemsize):", element_item_size, "bytes")
