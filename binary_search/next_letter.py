def search_next_letter(letters, key):
  len_letters = len(letters)
  start, end = 0, len(letters) - 1

  while start <= end:
    mid = start + (end-start)//2
    print('start = {},{}, mid = {},{}, end = {},{}'.format(start, letters[start], mid, letters[mid], end, letters[end]))

    if key == letters[mid]:
      return letters[(mid+1)%len_letters]

    if key < letters[mid]:
        end = mid - 1
    else:
        start = mid + 1
  return letters[(end+1)%len_letters]



print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
