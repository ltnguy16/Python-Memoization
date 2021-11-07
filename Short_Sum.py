#return the shortest route for the sum of the value

def short_sum(value, lst, memo):
  if value in memo:
    return memo[value]
  if value == 0:
    return []
  if value < 0:
    return None
  
  short_route = None
  
  for i in lst:
    remainder = value - i
    remainder_result = short_sum(remainder, lst, memo)
    if remainder_result != None:
      route = [*remainder_result, i]
      if short_route == None or len(route) < len(short_route):
        short_route = route
  memo[value] = short_route
  return memo[value]

"""
print(short_sum(100, [1,2,5,25], dict()))
print(short_sum(7, [5,4,3,7], dict()))
"""