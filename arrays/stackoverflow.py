values = ["one", "two", [], 6]

def count_str(values):
  index = 0
  counter = 0
  while index <= len(values)-1:
    if type(values[index]) == str:
      counter += 1
    index += 1
  return counter

ans = count_str(values)
print(ans)