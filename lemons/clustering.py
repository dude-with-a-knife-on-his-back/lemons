import lemons
from lemons import math
from lemons import os
from lemons import sp
from lemons import random


class clustering:

  class knn(preset):
    def __init__(self, class_size, dataset_train, dataset_test, k):
      # dataset_train, dataset_test must be: last val label
      self.dataset_train = dataset_train
      self.dataset_test = dataset_test
      if k == 0:
        self.epoch = True
        # K 0 sets auto k finding
      else:
        self.epoch = k
      self.class_size = class_size
      self.data_labels = []
      for data_point in dataset_train:
        self.data_labels.append(data_point[-1])

    def train(self, show=False):
      acc_pred = 0
      right_acc = 0
      curr_acc = 0
      curr_acc_list = []
      for index_val, val in enumerate(self.dataset_train):
        other = self.dataset_train
        other.pop(other.index(val))
        near_list = []
        near_label = []
        for comp in other:
          nearest = lemons.utils.matrix_distance(val[0], comp[0])
          near_list.append(nearest.get())
          near_label.append(index_val)
        org_near_list = sorted(near_list)
        if not self.epoch:
          pass # MAKE AUTO K HERE
        else:
          values = org_near_list[:self.epoch]
          values_class = []
          for val_cla in values:
            item_dataset = self.dataset_train[near_label[near_list.index(val_cla)]]
            values_class.append(item_dataset[-1])
          label = max(set(values_class), key = values_class.count)
          last_val_ = val[-1]
          if label == val[-1]:
            acc_pred += 1
            right_acc += 1
          else:
            right_acc += 1
          curr_acc = acc_pred / right_acc
          curr_acc_list.append(curr_acc)
          if show:
            print(f"predicted: {label}, actual: {last_val_}, nearest neighbours: {values_class}, current accuracy: {curr_acc}")
          else:
            pass
      acc = acc_pred / right_acc
      print(f"right predicts: {acc_pred}, total predicts: {right_acc}, accuracy: {acc}")
      return acc_pred, right_acc, curr_acc_list, acc
    
    def test(self, show=False):
      acc_pred = 0
      right_acc = 0
      curr_acc = 0
      curr_acc_list = []
      for index_val, val in enumerate(self.dataset_test):
        other = self.dataset_test
        other.pop(other.index(val))
        near_list = []
        near_label = []
        for comp in other:
          nearest = lemons.utils.matrix_distance(val[0], comp[0])
          near_list.append(nearest.get())
          near_label.append(index_val)
        org_near_list = sorted(near_list)
        if not self.epoch:
          pass # MAKE AUTO K HERE
        else:
          values = org_near_list[:self.epoch]
          values_class = []
          for val_cla in values:
            item_dataset = self.dataset_test[near_label[near_list.index(val_cla)]]
            values_class.append(item_dataset[-1])
          label = max(set(values_class), key = values_class.count)
          last_val_ = val[-1]
          if label == val[-1]:
            acc_pred += 1
            right_acc += 1
          else:
            right_acc += 1
          curr_acc = acc_pred / right_acc
          curr_acc_list.append(curr_acc)
          if show:
            print(f"predicted: {label}, actual: {last_val_}, nearest neighbours: {values_class}, current accuracy: {curr_acc}")
          else:
            pass
      acc = acc_pred / right_acc
      print(f"right predicts: {acc_pred}, total predicts: {right_acc}, accuracy: {acc}")
      return acc_pred, right_acc, curr_acc_list, acc
      
    def pred(self, pred_list):

  class svm(preset):

"""
Affinity Propagation
Agglomerative Clustering
BIRCH
DBSCAN
K-Means
Mini-Batch K-Means
Mean Shift
OPTICS
Spectral Clustering
Gaussian Mixture Model
Expectation–Maximization (EM) Clustering using Gaussian Mixture Models (GMM)
Agglomerative Hierarchical Clustering
"""
