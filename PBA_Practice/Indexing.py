# ======================== NUMPY INDEXING - THEORY ========================
#
# Indexing means accessing elements by position.
# In Python/NumPy:
# - Index starts from 0
# - Negative index starts from end
#   -1 means last element, -2 means second last, etc.
#
# =======================================================================

import numpy as np


# Given array from the question
arr = np.array([10, 20, 30, 40, 50])


# 1) First element of array
first_element = arr[0]

# 2) Last element using negative indexing
last_element = arr[-1]

# 3) Element at index 3
element_index_3 = arr[3]

# 4) Second element
second_element = arr[1]


# ======================== OUTPUT SECTION ========================
if __name__ == "__main__":
	print("Given Array:", arr)
	print()

	print("1) First element (arr[0]):", first_element)
	print("2) Last element using negative indexing (arr[-1]):", last_element)
	print("3) Element at index 3 (arr[3]):", element_index_3)
	print("4) Second element (arr[1]):", second_element)
