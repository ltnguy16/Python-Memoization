#return a dict with value that add up to the target value
def how_sum(value, lst, memo):
  if value in memo:
    return memo[value]
  if value == 0:
    return []
  if value < 0:
    return None
  for i in lst:
    remainder = value - i
    remainder_result = how_sum(remainder, lst, memo)
    if remainder_result != None:
      memo[value] = [*remainder_result, i]
      return memo[value]
  return None

"""
print(how_sum(7, [2,3], dict()))
print(how_sum(7, [5,3,4,7], dict()))
print(how_sum(8, [2,3,5], dict()))
"""