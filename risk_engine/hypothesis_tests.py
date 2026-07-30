#t=trading days, B= number of breaches and p=probability
def POF_test(t,B,alpha1,alpha2):
  df=1
  obs_rate = B/t
  #under null
  L0=((1-alpha1)**(t-B))*alpha1**B
  #under alternative
  L1=((1-obs_rate)**(t-B))*obs_rate**B

  t_stat = -2*np.log(L0/L1)
  critical_value = chi2.ppf(1 - alpha2, df)
  p_value = 1 - chi2.cdf(t_stat, df=1)
  if t_stat>=critical_value:
    print(f"refect H0 and accept H1")
  else:
    print(f"Do not reject H0")
  return p_value

#B is number of breaches
def CIT(B,alpha):
  #check yesterday and today for transition matrix
  k=np.array(B)
  n00= sum((k[:-1]==0) & (k[1:]==0))
  n01 = sum((k[:-1]==0) & (k[1:]==1))
  n10 = sum((k[:-1]==1) & (k[1:]==0))
  n11=sum((k[:-1]==1) & (k[1:]==1))

  t_matrix = np.array([[n00,n01],
                       [n10,n11]])

  o_b_prob=(n01+n11)/(n00+n01+n10+n11)
  b_prob_n_b_y =n01/(n00+n01)
  b_prob_b_y =n11/(n10+n11)

  #under null
  L0 = (1-o_b_prob)**(n00+n10)*o_b_prob**(n01+n11)
  #under alternate
  L1= ((1-b_prob_n_b_y)**n00)*(b_prob_n_b_y**n01)*((1-b_prob_b_y)**n10)*b_prob_b_y**n11

  Test_stat=-2*np.log(L0/L1)
  critical_value = chi2.ppf(1 - alpha, df=1)
  p_value = 1 - chi2.cdf(Test_stat, df=1)

  if Test_stat>=critical_value:
    print(f"refect H0 and accept H1")
  else:
    print(f"Do not reject H0")
  return p_value

