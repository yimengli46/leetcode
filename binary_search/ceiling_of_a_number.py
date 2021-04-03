def search_ceiling_of_a_number(arr, key):
  start, end = 0, len(arr) - 1

  if arr[end] < key:
  	return -1

  while start <= end:
    mid = start + (end-start)//2
    print('start = {},{}, mid = {},{}, end = {},{}'.format(start, arr[start], mid, arr[mid], end, arr[end]))

    if key == arr[mid]:
      return mid

    if key < arr[mid]:
        end = mid - 1
    else:
        start = mid + 1

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
  # we are not able to find the element in the given array, so the next big number will be arr[start]
  return start



print(search_ceiling_of_a_number([4, 6, 10], 6))
print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
print(search_ceiling_of_a_number([4, 6, 10], 17))
print(search_ceiling_of_a_number([4, 6, 10], -1))