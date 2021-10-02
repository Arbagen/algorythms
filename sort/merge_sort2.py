import random

def merge_sort(list):
  if len(list) <= 1:
   return list

  middle = len(list) // 2
  left_list = merge_sort(list[:middle])
  right_list = merge_sort(list[middle:])

  sorted_list = []
  left_index = 0
  right_index = 0
  while left_index < len(left_list) and right_index < len(right_list):
    if left_list[left_index] < right_list[right_index]:
      sorted_list.append(left_list[left_index])
      left_index += 1
    else:
      sorted_list.append(right_list[right_index])
      right_index += 1
  sorted_list += left_list[left_index:]
  sorted_list += right_list[right_index:]
  return sorted_list

numbers = list(range(1, 1000))
random.shuffle(numbers)
result = merge_sort(numbers)
print(result)