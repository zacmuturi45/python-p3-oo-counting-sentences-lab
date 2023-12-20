#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self._value = value
    

  def get_value(self):
    return self._value
  
  def set_value(self, new_value):
    if type(new_value) != str:
      print("The value must be a string.")
    else:
      self._value = new_value

  value = property(get_value, set_value)

  def is_sentence(self):
    if self._value[-1] == '.':
      return True
    else:
      return False
    
  def is_question(self):
    if self._value[-1] == '?':
      return True
    else:
      return False

  def is_exclamation(self):
    if self._value[-1] == '!':
      return True
    else:
      return False    
    
  def count_sentences(self):
    empty = []
    quote = ('!.?')
    new_string = self._value.split()
    m = 0
    while m < len(new_string):
      if new_string[m][-1] in quote:
        empty.append(new_string[m])
        m = m + 1
      else:
        m = m +1
    return len(empty)

    


