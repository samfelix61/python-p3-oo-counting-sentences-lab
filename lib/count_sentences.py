#!/usr/bin/env python3

import re

import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Split the value by punctuation that could indicate the end of a sentence
        sentences = re.split(r'[.!?]', self._value)
        # Filter out empty strings
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

# Example usage:
my_string = MyString("Hello world! Is this a question? Yes, it is a sentence.")
print(my_string.is_exclamation())  # Output: False
print(my_string.is_question())     # Output: False
print(my_string.is_sentence())     # Output: True

my_string.value = "Hello world! How are you? This is great!"
print(my_string.is_exclamation())  # Output: True
print(my_string.count_sentences()) # Output: 3

try:
    my_string.value = 123  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: The value must be a string.


