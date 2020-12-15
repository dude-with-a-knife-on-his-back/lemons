import lemons
from lemons import math
from lemons import os
from lemons import sp
from lemons import random

class proj:
  def __init__(self,deps_list, user, project, git, gitrep, description):
    self.deps_list = deps_list
    self.user = user
    self.project = project
    self.git = git
    self.gitrep = gitrep
    self.description = description

  def deps(self):
    dependencies = self.deps_list 
    return dependencies
  
  def deps_pip(self):
    dependencies = self.deps_list 
    status = {}
    for i in dependencies:
      os.system(f"pip install {i}")
      stat = sp.getoutput(f"pip install {i}")
      status[i] = stat
    return status
  
  def config(self, user, project, git, gitrep, description):
    self.user = user
    self.project = project
    self.git = git
    self.gitrep = gitrep
    self.description = description
    print(f"username: {self.user} \n project: {self.project}\n git: {self.git}\n gitrep: {self.gitrep}\n description: {self.description}")
  
  