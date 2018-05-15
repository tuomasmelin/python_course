#!/usr/bin/env python

class Person(object):
  """A persons base class. Persons have the
    following properties:

    Attributes:
        first_name: A string representing the persons's first name.
        last_name: A string representing the persons's last name.
        social_security_number: A string of the persons social security number.
    """

  def __init__(self, first_name, last_name, social_security_number):
    """Return a Person object""" 
    self.first_name = first_name
    self.last_name = last_name
    self.social_security_number = social_security_number

    print('Created a new person: %s %s' % (first_name, last_name))

  def get_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    

class Employee(Person):
  def __init__(self, first_name, last_name, social_security_number, salary):
    self.first_name = first_name
    self.last_name = last_name
    self.social_security_number = social_security_number
    self.salary = salary

    print ('Created a new employee: %s %s' % (first_name, last_name))

  def get_salary(self):
    return self.salary
    

if __name__ == "__main__":
    tmelin = Person('Tuomas', 'Melin', '123456')
    emp = Employee('Some', 'Other', '7890123', 1000)

    print tmelin.get_name()
    print emp.get_name()
    print emp.get_salary()