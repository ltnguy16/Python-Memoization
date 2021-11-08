#return true or false if the string can be constructed
def can_construct(target, wordBank, memo):
  if target in memo:
    return memo[target]
  if target == "":
    return True
  for word in wordBank:
    if target.startswith(word):
      if can_construct(target[len(word):], wordBank, memo) == True:
        memo[target] = True
        return memo[target]
  return False

print(can_construct("string", ["st", "sh", "ng", "ir", "ri"], dict()))
print(can_construct("string", ["st", "sh", "ng", "ir", "r"], dict()))

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], dict()))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], dict()))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], dict()))