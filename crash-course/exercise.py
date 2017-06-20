from __future__ import division

# FUNCTIONS (don't forget the colon)

def double(x):
  return x * 2

# Functions are first-class citizens
def apply_to_one(f):
  return f(1)

my_double = double
x = apply_to_one(my_double)

# Anonymous functions can be declared with lambda (don't forget the colon)
y = apply_to_one(lambda x: x + 4)

def another_double(x): return 2* x

# Default value declarations identical to JS
def my_print(message='my default message'):
  print message

my_print('hello')
my_print()

def difference(a=0, b=0):
  return a - b

print difference(10, 5)
print difference(0, 5)
print difference(b=5) # arguments can be specified on call

# STRINGS

# Use raw to escape characters
print r'\n'

# multiline strings with triple quotes
multi_line = '''First line.
Second line.
Third line.'''

print multi_line

# EXCEPTIONS

try:
  print 0 / 0
except ZeroDivisionError: # explicit exceptions much case-match error
# except: # general exceptions invoked like this
  print 'cannot divide by zero, ya dingus'

# LISTS
# Similar to arrays but with added functionality

integer_list = [1, 2, 3]
heterogeneous_list = ['string', 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

list_length = len(integer_list)
print list_length
list_sum = sum(integer_list)
print list_sum

a = range(10) # Creates a list of integers 0 through 9
zero = a[0]   # lists are 0-indexed
one = a[1]
nine = a[-1]  # list[-1] is pythonic for last element
eight = a[-2] # you guessed it, list[-2] is for second to last element

# Slicing lists
first_three = a[:3]
three_to_end = a[3:]
one_to_four = a[1:5] # last argument is non-inclusive
last_three = a[-3:]
without_first_and_last = a[1:-1]
copy_of_a = a[:]

# List membership

print 1 in [1, 2, 3]
print 0 in [1, 2, 3]

# Concatenation

b = [1, 2, 3]
b.extend([4, 5, 6])
print b

