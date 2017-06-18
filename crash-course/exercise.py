from __future__ import division

# Functions

def double(x):
  return x * 2

def apply_to_one(f):
  return f(1)

my_double = double
x = apply_to_one(my_double)

y = apply_to_one(lambda x: x + 4)

def another_double(x): return 2* x

def my_print(message='my default message'):
  print message

my_print('hello')
my_print()

def difference(a=0, b=0):
  return a - b

print difference(10, 5)
print difference(0, 5)
print difference(b=5)

