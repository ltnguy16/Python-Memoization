#return all the path that can construct the string

def all_construct(target, wordBank, memo):
  if target in memo:
    return memo[target]
  if target == '':
    return [[]]

  result = []

  for word in wordBank:
    if target.startswith(word):
      result += [[word] + x for x in all_construct(target[len(word):], wordBank, memo)]
      memo[target] = result
  return result

print(all_construct("string", ["st", "sh", "ng", "ir", "ri"], dict()))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"], dict()))
print(all_construct("abcdef", ["b", "a", "c", "t", "f", "z"], dict()))
print(all_construct("", ["b", "a", "c", "t", "f", "z"], dict()))


