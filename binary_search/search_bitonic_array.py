def search_bitonic_array(arr, key):
	max_idx = find_max_index_in_bitonic_array(arr)

	# search in the first half
	first_half_idx = binary_search(arr[:max_idx+1], key)
	if first_half_idx > -1:
		return first_half_idx
	second_half_idx = binary_search(arr[max_idx+1:], key)
	if second_half_idx > -1:
		return max_idx + 1 + second_half_idx


	return -1

def find_max_index_in_bitonic_array(arr):
  start, end = 0, len(arr) - 1

  while start < end:
  	mid = start + (end - start)//2
  	if arr[mid] > arr[mid+1]:
  		end = mid
  	else:
  		start = mid+1
  
  # at the end of the while loop, start==end
  return start

def binary_search(arr, key):
  start, end = 0, len(arr) - 1
  isAscending = arr[start] < arr[end]
  while start <= end:
  	mid = start + (end-start)//2

  	if key == arr[mid]:
  		return mid

  	if isAscending:
  		if key < arr[mid]:
  			end = mid - 1
  		else:
  			start = mid + 1
  	else:
  		if key > arr[mid]:
  			end = mid - 1
  		else:
  			start = mid + 1

  return -1


print(search_bitonic_array([1, 3, 8, 4, 3], 4))
print(search_bitonic_array([3, 8, 3, 1], 8))
print(search_bitonic_array([1, 3, 8, 12], 12))
print(search_bitonic_array([10, 9, 8], 10))