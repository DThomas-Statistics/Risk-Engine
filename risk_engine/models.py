ef hist_risk(percent_vec,alpha):
  if len(percent_vec) <100:
    print(f"lack of data may lead to insufficient statistical reliability")
  w = np.sort(percent_vec)
  q = int(np.floor(alpha*len(percent_vec)))
  VaR = abs(w[q])

#move onto expected shortfall completing our historical risk fucntion
  E_SF = abs(np.mean(w[:q]))
  print(f"The historical {alpha*100}% VaR for {len(percent_vec)} days is: {VaR}")
  print(f"The historical {alpha*100}% Expected shortfall for {len(percent_vec)} days is: {E_SF}")
  return VaR, E_SF

def normal_riskp(value, alpha, weight, percent):
  #drift = np.mean(port_vec)
  #vol = np.sd(port_vec)
  sd =  np.sqrt(weight.T@np.cov(percent, rowvar=True)@ weight)
  VaR = -sd*norm.ppf(alpha)*value

  #ES
  ES= sd*norm.pdf(norm.ppf(alpha))/alpha *value

  print(f"The normal {alpha*100}% VaR for {percent.shape[1]} days is: {VaR}")
  print(f"The normal {alpha*100}% Expected shortfall for {percent.shape[1]} days is: {ES}")
  return VaR, ES

ef student_risk(value, alpha, weight, percent, kurtosis):
  DF = (6/kurtosis)+4
  sd =  np.sqrt(weight.T@np.cov(percent, rowvar=True)@ weight)
  VaR = -sd*t.ppf(alpha,DF)*value

  #ES
  ES = sd*(t.pdf(t.ppf(alpha,DF),DF)/alpha)*((DF+ t.ppf(alpha,DF)**2)/(DF-1))*value
  print(f"The t dist {alpha*100}% VaR for {percent.shape[1]} days is: {VaR}")
  print(f"The t dist {alpha*100}% Expected shortfall for {percent.shape[1]} days is: {ES}")
  return VaR, ES

def EWMA(percent, weight, value, alpha):
  T = percent.shape[1]
  l = 0.94
  cov =  np.cov(percent, rowvar=True)
  for t in range(1,T):
    returns_at_t_minus_1 = percent[:, t-1].reshape(-1, 1) # Make it a column vector
    cov = l * cov + (1 - l) * (returns_at_t_minus_1 @ returns_at_t_minus_1.T)

  sigma = np.sqrt(weight.T@cov@weight)
  VaR = -sigma*norm.ppf(alpha)*value
  return VaR
