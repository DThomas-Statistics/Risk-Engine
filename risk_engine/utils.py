import numpy as np

def portfolio_vec(weight, price_matrix):
  percent=(price_matrix[:, 1:] - price_matrix[:, :-1]) / price_matrix[:, :-1]
  percent[percent == 0.0] = 1e-8
  port_vec = np.dot(weight,price_matrix)
  percent_vec = np.dot(weight,percent)
  return percent,port_vec, percent_vec

