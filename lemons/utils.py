import lemons
from lemons import math
from lemons import os
from lemons import sp
from lemons import random

class utils:
  euler_constant = 2.71828

  pi = 3.14159
  
  pi32 = 3.14159265358979323846264338327950

  pi64 = 3.1415926535897932384626433832795028841971693993751058209749445923

  def list_prod(list_to_prod):
    val = 1
    for i in list_to_prod:
      val *= i
    return val

  class matrix:
    def __init__(self, shape, values):
      self.shape = shape
      # [3,4,2]
      self.reversed_shape = shape[::-1]
      self.values = values
      # for a matrix as such:
      # [[[0,1],
        # [1,0],
        # [0,1],
        # [1,0]],
        # [[0,1],
        # [1,0],
        # [0,1],
        # [1,0]],
        #[[0,1],
        # [1,0],
        # [0,1],
        # [1,0]]]
      # the values shall be like this [0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0]
      #

    def gen(self):
      
      return matrix
    
    def dimensions(self):
      return len(self.shape) + 1

    class random_matrix:

    
      def __init__(self, shape, min_value, max_value):
        self.shape = shape
        self.min_value = min_value
        self.max_value = max_value

      def get(self):
        random_ints = []
        for i in range(lemons.utils.list_prod(self.shape)):
          random_value = random.randint(self.min_value, self.max_value)
          random_ints.append(random_value)
        matrix = lemons.utils.matrix_gen.get(self.shape,random_ints)
        return matrix

  class matrix_distance:
    def __init__(self, point1, point2):
      wrong_dim = lemons.error("dimensions dont match")
      if len(point1) == len(point2):
        self.point1 = point1
        self.point2 = point2
        self.dimensions = len(point1)
      else:
        wrong_dim.custom()
      
    def get(self):
      distance = 0.0
      for i in range(self.dimensions):
        sub = self.point1[i] - self.point2[i]
        distance += (sub * sub)
      return math.sqrt(distance)



