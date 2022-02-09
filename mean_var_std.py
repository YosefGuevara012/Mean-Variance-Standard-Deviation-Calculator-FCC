import numpy as np

def calculate(list):

##  Reshaping the list to a matrix
  print(len(list))

  if len(list) != 9:

    return "List must contain nine numbers."

  else:

    my_array = np.array(list)
    my_matrix = my_array.reshape(3,3)
    calculations ={

    'mean': mean(my_matrix),
    'variance': variance(my_matrix),
    'standard deviation':std(my_matrix),
    'max': max(my_matrix),
    'min': min(my_matrix),
    'sum': sum(my_matrix),
    }

    return calculations
  


  

def mean(matrix):

  axis1 = matrix.mean(axis = 0)
  axis2 = matrix.mean(axis = 1)
  flattened = matrix.mean()

  return [list(axis1), list(axis2), flattened]

def variance(matrix):

  axis1 = matrix.var(axis = 0)
  axis2 = matrix.var(axis = 1)
  flattened = matrix.var()

  return [list(axis1), list(axis2), flattened]

def std(matrix):

  axis1 = matrix.std(axis = 0)
  axis2 = matrix.std(axis = 1)
  flattened = matrix.std()

  return [list(axis1), list(axis2), flattened]

def max(matrix):

  axis1 = matrix.max(axis = 0)
  axis2 = matrix.max(axis = 1)
  flattened = matrix.max()

  return [list(axis1), list(axis2), flattened]

def min(matrix):

  axis1 = matrix.min(axis = 0)
  axis2 = matrix.min(axis = 1)
  flattened = matrix.min()

  return [list(axis1), list(axis2), flattened]

def sum(matrix):

  axis1 = matrix.sum(axis = 0)
  axis2 = matrix.sum(axis = 1)
  flattened = matrix.sum()

  return [list(axis1), list(axis2), flattened] 