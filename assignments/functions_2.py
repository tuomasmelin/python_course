#!/usr/bin/env python

def add_one(variable):
  """
    Adds one to the parameter value.
  """
  return variable + 1

def add_five(variable):
  """
    Adds five to the parameter value.
  """
  return variable + 5

def add_three(variable):
  """
    Adds three to the parameter value.
  """
  return variable + 3

def count_function():
  """
    Returns result of all calculations.
  """
  result_1 = 0
  result_2 = add_one(result_1) 
  result_3 = add_five(result_2)
  final_result = add_three(result_3)
  return final_result

if __name__ == "__main__":
  print_result = count_function() 
  print(print_result) 