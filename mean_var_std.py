import numpy as np

def calculate(list):

##  Reshaping the list to a matrix
  my_array = np.array(list)
  my_matrix = my_array.reshape(3,3)

  
  print("AQUI")
  print(mean(my_matrix))


  # return calculations

def mean(matrix):

  axis1 = matrix.mean(axis = 0)
  axis2 = matrix.mean(axis = 1)
  flattened = (axis1.mean() + axis2.mean()) / 2

  return [list(axis1), list(axis2), flattened]