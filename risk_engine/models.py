def hist_risk(percent_vec,alpha):
  if len(percent_vec) <100:
    print(f"lack of data may lead to insufficient statistical reliability")
  w = np.sort(percent_vec)
  q = int(np.floor(alpha*len(percent_vec)))
  VaR = abs(w[q])

#move onto expected shortfall completing our historical risk fucntion
  E_SF = abs(np.mean(w[:q]))
  #print(f"The historical {alpha*100}% VaR for {len(percent_vec)} days is: {VaR}")
  #print(f"The historical {alpha*100}% Expected shortfall for {len(percent_vec)} days is: {E_SF}")
  return VaR, E_SF

def normal_riskp(alpha, percent_vec):
  #drift = np.mean(port_vec)
  sd = np.std(percent_vec)
  #sd =  np.sqrt(weight.T@np.cov(percent_vec, rowvar=True)@ weight)
  VaR = -sd*norm.ppf(alpha)

  #ES
  ES= sd*norm.pdf(norm.ppf(alpha))/alpha

  #print(f"The normal {alpha*100}% VaR for {percent_vec.shape[1]} days is: {VaR}")
  #print(f"The normal {alpha*100}% Expected shortfall for {percent_vec.shape[1]} days is: {ES}")
  return VaR, ES

def student_risk(alpha, percent_vec):
  mean=np.mean(percent_vec)
  avg_fourth = np.mean((percent_vec-mean)**4)
  std = np.std(percent_vec)**4
  E_kurtosis = avg_fourth/std
  kurtosis= E_kurtosis-3
  DF = (6/kurtosis)+4
  sd=np.std(percent_vec)
  #sd =  np.sqrt(weight.T@np.cov(percent_vec, rowvar=True)@ weight)
  VaR = -sd*t.ppf(alpha,DF)

  #ES
  ES = sd*(t.pdf(t.ppf(alpha,DF),DF)/alpha)*((DF+ t.ppf(alpha,DF)**2)/(DF-1))
  #print(f"The t dist {alpha*100}% VaR for {percent_vec.shape[1]} days is: {VaR}")
  #print(f"The t dist {alpha*100}% Expected shortfall for {percent_vec.shape[1]} days is: {ES}")
  return VaR, ES


def findGARCH(percent_vec):
  #the goal here is to create a function taht will use AIC to find an optimum GARCH based model
  GARCH_model_N_1 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=1, o=0, power= 2.0, dist = 'normal', rescale = False)
  GARCH_model_t_1 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=1, o=0, power= 2.0, dist = 'StudentsT', rescale = False)
  GARCH_model_N_2 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=2, q=1, o=0, power= 2.0, dist = 'normal', rescale = False)
  GARCH_model_t_2 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=2, q=1, o=0, power= 2.0, dist = 'StudentsT', rescale = False)
  GARCH_model_N_3 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=2, o=0, power= 2.0, dist = 'normal', rescale = False)
  GARCH_model_t_3 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=2, o=0, power= 2.0, dist = 'StudentsT', rescale = False)
  EGARCH_t = arch_model(percent_vec,mean = 'constant', lags=0, vol='EGARCH', p=1, q=1, o=1, dist = 'StudentsT', rescale = False)
  EGARCH_N = arch_model(percent_vec,mean = 'constant', lags=0, vol='EGARCH', p=1, q=1, o=1, dist = 'Normal', rescale = False)
  TGARCH_model_t_1 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=1, o=1, power= 1.0, dist = 'StudentsT', rescale = False)
  TGARCH_model_N_2 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=2, q=1, o=1, power= 1.0, dist = 'normal', rescale = False)
  TGARCH_model_t_2 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=2, q=1, o=1, power= 1.0, dist = 'StudentsT', rescale = False)
  TGARCH_model_N_3 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=2, o=1, power= 1.0, dist = 'normal', rescale = False)
  TGARCH_model_t_3 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=2, o=1, power= 1.0, dist = 'StudentsT', rescale = False)
  GJR_GARCH_t_1 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=1, o=1, power= 2.0, dist = 'StudentsT', rescale = False)
  GJR_GARCH_N_1 = arch_model(percent_vec,mean = 'constant', lags=0, vol = 'GARCH', p=1, q=1, o=1, power= 2.0, dist = 'Normal', rescale = False)

  GARCH_model_N_1=GARCH_model_N_1.fit(disp='off')
  GARCH_model_N_2=GARCH_model_N_2.fit(disp='off')
  GARCH_model_N_3=GARCH_model_N_3.fit(disp='off')
  GARCH_model_t_1=GARCH_model_t_1.fit(disp='off')
  GARCH_model_t_2=GARCH_model_t_2.fit(disp='off')
  GARCH_model_t_3=GARCH_model_t_3.fit(disp='off')
  EGARCH_t=EGARCH_t.fit(disp='off')
  EGARCH_N=EGARCH_N.fit(disp='off')
  TGARCH_model_t_1=TGARCH_model_t_1.fit(disp='off')
  TGARCH_model_N_2=TGARCH_model_N_2.fit(disp='off')
  TGARCH_model_t_2=TGARCH_model_t_2.fit(disp='off')
  TGARCH_model_N_3=TGARCH_model_N_3.fit(disp='off')
  TGARCH_model_t_3=TGARCH_model_t_3.fit(disp='off')
  GJR_GARCH_t_1=GJR_GARCH_t_1.fit(disp='off')
  GJR_GARCH_N_1=GJR_GARCH_N_1.fit(disp='off')





  models = {"GARCH_model_N_1":(GARCH_model_N_1.loglikelihood,GARCH_model_N_1.num_params),
            "GARCH_model_N_2":(GARCH_model_N_2.loglikelihood,GARCH_model_N_2.num_params),
            "GARCH_model_N_3":(GARCH_model_N_3.loglikelihood,GARCH_model_N_3.num_params),
            "GARCH_model_t_1":(GARCH_model_t_1.loglikelihood,GARCH_model_t_1.num_params),
            "GARCH_model_t_2":(GARCH_model_t_2.loglikelihood,GARCH_model_t_2.num_params),
            "GARCH_model_t_3":(GARCH_model_t_3.loglikelihood,GARCH_model_t_3.num_params),
            "EGARCH_t":(EGARCH_t.loglikelihood,EGARCH_t.num_params),
            "EGARCH_N":(EGARCH_N.loglikelihood,EGARCH_N.num_params),
            "TGARCH_model_t_1":(TGARCH_model_t_1.loglikelihood,TGARCH_model_t_1.num_params),
            "TGARCH_model_N_2":(TGARCH_model_N_2.loglikelihood,TGARCH_model_N_2.num_params),
            "TGARCH_model_t_2":(TGARCH_model_t_2.loglikelihood,TGARCH_model_t_2.num_params),
            "TGARCH_model_N_3":(TGARCH_model_N_3.loglikelihood,TGARCH_model_N_3.num_params),
            "TGARCH_model_t_3":(TGARCH_model_t_3.loglikelihood,TGARCH_model_t_3.num_params),
            "GJR_GARCH_t_1":(GJR_GARCH_t_1.loglikelihood,GJR_GARCH_t_1.num_params),
            "GJR_GARCH_N_1":(GJR_GARCH_N_1.loglikelihood,GJR_GARCH_N_1.num_params)}

  scoreS = {}
  fitted_objects = {
        "GARCH_model_N_1": GARCH_model_N_1, "GARCH_model_N_2": GARCH_model_N_2, "GARCH_model_N_3": GARCH_model_N_3,
        "GARCH_model_t_1": GARCH_model_t_1, "GARCH_model_t_2": GARCH_model_t_2, "GARCH_model_t_3": GARCH_model_t_3,
        "EGARCH_t": EGARCH_t, "EGARCH_N": EGARCH_N,
        "TGARCH_model_t_1": TGARCH_model_t_1, "TGARCH_model_N_2": TGARCH_model_N_2, "TGARCH_model_t_2": TGARCH_model_t_2,
        "TGARCH_model_N_3": TGARCH_model_N_3, "TGARCH_model_t_3": TGARCH_model_t_3,
        "GJR_GARCH_t_1": GJR_GARCH_t_1, "GJR_GARCH_N_1": GJR_GARCH_N_1}

  for name, (ll,n) in models.items():
    AIC = 2*n -2*ll

    BIC = n*np.log(len(percent_vec))- 2*ll
    scoreS[name] = {"AIC": AIC, "BIC": BIC}

    #getting the optimal model via smallest AIC value
  o_modelA = min(scoreS, key=lambda m: scoreS[m]["AIC"])
  o_modelB = min(scoreS, key=lambda m: scoreS[m]["BIC"])
  
  if o_modelA!=o_modelB:
      print("AIC and BIC do not agree so we will use model following BIC as its stricter")
      chosen_model = o_modelB
      return fitted_objects[chosen_model]
  else:
    print(f"agreeing AIC and BIC so {o_modelA}")
    chosen_model = o_modelA


    return fitted_objects[chosen_model]


def compute_garch_risk(o_model, alpha,window):
  vol_type = o_model.model.volatility.name
  dist_type = o_model.model.distribution.name
  power_val = getattr(o_model.model.volatility, 'power', 2.0)
  Model = arch_model(window,mean = 'constant', lags=0, vol = vol_type, p=o_model.model.volatility.p, q=o_model.model.volatility.q, o=o_model.model.volatility.o, power=power_val, dist = dist_type, rescale = True)
  res=Model.fit()
  vol_type = res.model.volatility
  #DF = res.params['nu']
  forecasts = res.forecast()
  f_v=forecasts.variance.iloc[-1,0]
  f_SD =np.sqrt(f_v)
  #VaR_N= f_SD*norm.ppf(alpha)*value
  #VaR_t=f_SD*t.ppf(alpha,DF)*value
  #VaR_N_over_days = VaR_N*np.sqrt(T)
  #VaR_t_over_days = VaR_t*np.sqrt(T)

  #ES
  #ES_t = f_SD*(t.pdf(t.ppf(alpha,DF),DF)/alpha)*((DF+ t.ppf(alpha,DF)**2)/(DF-1))*value
  #ES_N= -*f_SD*norm.pdf(norm.ppf(alpha))/alpha *value
  #Now consider multio day VaR
  #ES_t_over_days = ES_t *np.sqrt(T)
  #ES_N_over_days =ES_N * np.sqrt(T)


  if 'nu' in res.params:
    DF = res.params['nu']
    VaR_t=-f_SD*t.ppf(alpha,DF)
    VaR_t_over_days = VaR_t
    ES_t = f_SD*(t.pdf(t.ppf(alpha,DF),DF)/alpha)*((DF+ t.ppf(alpha,DF)**2)/(DF-1))
    ES_t_over_days = ES_t 
    return VaR_t_over_days, ES_t_over_days, res

  else:
    VaR_N= -f_SD*norm.ppf(alpha)
    VaR_N_over_days = VaR_N
    ES_N= f_SD*norm.pdf(norm.ppf(alpha))/alpha 
    ES_N_over_days =ES_N
    return VaR_N_over_days,ES_N_over_days, res


  #return VaR_N_over_days,VaR_t_over_days,ES_t_over_days,ES_N_over_days
