#return true or false after checking to see if the value given can be added up to by the value in the list

def canSum(value, lst, memo):
  if value in memo:
    return memo[value]
  if value == 0:
    return True
  if value < 0:
    return False
  for i in lst:
    if (canSum(value - i, lst, memo) == True):
      memo[value] = True
      return memo[value]
  memo[value] = False
  return False

value = 300
lst = [14,7]
print(canSum(value, lst, dict()))