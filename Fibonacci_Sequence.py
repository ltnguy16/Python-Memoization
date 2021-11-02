#Fibonacci Sequence with memoization

def fib(value, memo):
  if value in memo:
    return memo[value]
  elif value <= 2:
    return 1
  else:
    memo[value] = fib(value - 1, memo) + fib(value - 2, memo)
  return memo[value]

value = 199
print(fib(value, dict()))