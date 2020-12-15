import lemons
from lemons import math
from lemons import os
from lemons import sp
from lemons import random


class nn:
  class visuals:
    def __init__(self, project_name):
      self.project_name = project_name
      
    def cyan_lightgreen_bar():
      print(lemons.colors.Cyan, lemons.colors.BackgroundLightGreen,"_________________________________________________________________"lemons.colors.Default)
    def layer(color,type, number, input_shape, output_shape, amount):
      color_set = exec("lemons.colors.{color}")
      print(f"{color_set}{number}   {layer}    {input_shape}    {output_shape}    {amount}")
    def layer_inform():
      print(".number         layer         input_shape         output_shape         amount")
    def equal_bar():
      print("=================================================================")
    def hashtag_bar():
      print("#################################################################")
    def cool_bar():
      print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    def model_params(tot, train, test, non_train):
      print("total: {tot}")
      print("train: {train}")
      print("test: {test}")
      print("non-trainable: {non_train}")
    def project_name(self):
      print(f"            {self.project_name}              ")

  def __init__(self, layer_count, layer_type,input_shape, output_shape, amount):
    self.layer_count = layer_count
    self.layer_type = layer_type
    self.input_shape = input_shape
    self.output_shape = output_shape
    self.amount = amount = amount
    self.total_params = total_params
    self.training_params = training_params
    self.testing_params = testing_params
    self.non_training_params = non_training_params
    

  @classmethod
  def view_model(self, color_list=[], project_name):
    aesthetic = lemons.nn.visuals(project_name)
    aesthetic.project_name()
    aesthetic.cyan_lightgreen_bar()
    aesthetic.layer_inform()
    color_list = []
    if len(color_list) == 0:
      for i in range(self.layer_count):
        color_list.append(LightMagenta)
    for i in range(self.layer_count):
      color = color_list[i]
      aesthetic.layer( color, self.layer_type[i], self.layers[i], self.input_shape, self.output_shape, self.amount)
    aesthetic.equal_bar()
    aesthetic.model_params(self.total_params, self.training_params, self.testing_params, self.non_training_params)

    


  @classmethod
  def view_data():

  # ANN -> artificial nn. User says what the function will be for the neuron, then we do the rest
  # DNN -> ANN but its a lot of hidden layers
  # CNN
  # RNN 
  # autoencoder