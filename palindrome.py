import math
# 12345
# Level
# 01234
def is_palindrome():
  user_input = input()
  user_input = user_input.lower()
  user_list = []
  for i in user_input:
    if i != " ":
      user_list.append(i)
  for i in range(math.ceil(len(user_list)/2)):
    if user_list[i] != user_list[len(user_list)-i-1]:
      return False
  return True

print(is_palindrome())
