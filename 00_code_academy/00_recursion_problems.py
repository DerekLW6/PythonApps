#############################
#### Finding the Minimum ####
#############################
def find_min(my_list, min = None):
  if not my_list:
    return min

  if not min or my_list[0] < min:
    min = my_list[0]
  return find_min(my_list[1:], min)


#############################
    #### Sum Digits ####
#############################
def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit


###################
#### Fibonacci ####
###################
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

#####################
### Is Plaindrome ###
#####################

def is_palindrome(text):
  if len(text) < 2:
    return True
  else: 
    if text[0] != text[-1]:
      return False
    return is_palindrome(text[1:-1])

######################
### Multiplication ###
######################

def multiplication(num_a, num_b):
  if num_a == 0 or num_b == 0:
    return 0

  return num_a + multiplication(num_a, num_b - 1)


# test cases
# print(is_palindrome("abba") == True)
# print(is_palindrome("abcba") == True)
# print(is_palindrome("") == True)
# print(is_palindrome("axxxx") == False)

# test cases
# print(sum_digits(12) == 3)
# print(sum_digits(552) == 12)
# print(sum_digits(123456789) == 45)

# test cases
# print(find_min([42, 17, 2, -1, 67]) == -1)
# print(find_min([]) == None)
# print(find_min([13, 72, 19, 5, 86]) == 5)