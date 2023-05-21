#!/usr/bin/python3
from models.base_model import BaseModel
import json

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():

    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))

"""Return list of JSON string representation"""
list_input = [my_model.to_dict(), my_model.to_dict(), my_model.to_dict()]
list_output = BaseModel.to_json_string(list_input)
