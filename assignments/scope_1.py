#!/usr/bin/env python

# first we associate the name 'y' with the number 3
y = 3                                   

# then we associate the name print_function with this function
def print_function():              
  print "inside print_function"          
  print y                                                                              
  z = 4     
  print z                
  print "exiting print_function"


# we call print_function
print_function()  

# this works fine
print y

# NameError will result                            
print z