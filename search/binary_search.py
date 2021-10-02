from verify_search import verify

def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    midpoint = (first + last) // 2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None


numbers = range(1, 50)
verify(binary_search(numbers, 5))
verify(binary_search(numbers, 55))