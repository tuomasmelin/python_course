#!/usr/bin/env python

def example_function(parameter_1=0, parameter_2='default'):
  """ 
    functions can have default arguments
  """
  print ('inside example function')
  return parameter_2


if __name__ == "__main__":
  result = example_function() 
  print(result) 

  result = example_function(1) 
  print(result) 

  result = example_function(1, 'not_default') 
  print(result) 

  result = example_function(parameter_2='hello') 
  print(result) 

