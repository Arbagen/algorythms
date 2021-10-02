from verify_search import verify

def linear_search(list, target):
  for index in range(0, len(list)):
    if list[index] == target:
      return index
  return None

numbers = range(1, 10)
verify(linear_search(numbers, 3))
verify(linear_search(numbers, 11))