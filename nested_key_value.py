#!/usr/bin/env python
'''
Program to find the value from nested objects when the object and a key are passed to the function.
'''
import ast

input_dict_objects = input('Enter the nested objects in dictionary format: For eg. {"a": {"b": {"c": "d"}}} => ')
nested_objects = ast.literal_eval(input_dict_objects)
input_dict_key = input('Enter the key to be passed: For eg. a/b/c => ')

#Split the keys from input dictionary
no_keys = len([key for key in input_dict_key.split('/')])

get_dict_item = nested_objects

# Function to get values from a dictionary
def dict_value(dict_input):
    for (dict_key, dict_value) in dict_input.items():
        return dict_value

# Function to count number of dictionay values
def dict_value_count(dict_input):
    if not isinstance(dict_input, str):
        return dict_value(dict_input)

# Main program to manipulate the nested objects and find value for the key
for key_item in range(no_keys):
    get_dict_item = dict_value(get_dict_item)
    if key_item == ( no_keys - 1 ):
        print(get_dict_item)
