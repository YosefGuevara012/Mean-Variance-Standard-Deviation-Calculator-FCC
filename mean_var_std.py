import numpy as np

def calculate(list):

##  Reshaping the list to a matrix
  my_array = np.array(list)
  my_matrix = my_array.reshape(3,3)

  
  print("AQUI")
  print(stdv(my_matrix))


  # return calculations

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

def stdv(matrix):

  axis1 = matrix.std(axis = 0)
  axis2 = matrix.std(axis = 1)
  flattened = matrix.std()

  return [list(axis1), list(axis2), flattened]