#https://tutorialreference.com/python/examples/faq/python-how-to-find-index-of-element-of-list-that-meet-a-condition
#def first_drop_point(data_list, threshold):
 #   sorted_list = sorted(data_list)
 #   for idx, value in enumerate(sorted_list):
  #      if value < threshold:
  #          return idx
  #  return None

def first_drop_point(data_list, threshold):
    sorted_list = sorted(data_list)
    for idx, value in enumerate(sorted_list):
        if value > threshold:
            return idx
    return len(sorted_list) 
def ES_error(values, ES_val):
  sort_val = np.sort(values)

  n_H = first_drop_point(values, ES_val)
  below_vals = sort_val[:n_H]
  k_H = np.mean(below_vals)
  E_H = abs(k_H) - abs(ES_val)
  return E_H

def backtest(hist_percent_vec, BURNIN,alpha):
  ASSIST_FINDGARCH = hist_percent_vec[0:BURNIN]
  o_model=findGARCH(ASSIST_FINDGARCH)
  di = {"Date": [],
        "Simple_return": [],
        "N_breachoVaR": [],
        "T_breachoVaR": [],
        "H_breachoVaR": [],
        "G_breachoVaR": [],
        "N_ES": [],
        "T_ES": [],
        "H_ES": [],
        "G_ES": [],
        "N_VaR":[],
        "T_VaR":[],
        "H_VaR":[],
        "G_VaR":[],
        }

  BR_H=[]
  BR_N=[]
  BR_T=[]
  BR_G=[]
  ES_E_H=[]
  ES_E_N=[]
  ES_E_T=[]
  ES_E_G=[]
  for t in range(BURNIN,len(hist_percent_vec)):
    t1=t-BURNIN
    t2 =t
    window =hist_percent_vec[t1:t2]
    di["Simple_return"].append(hist_percent_vec[t])
    di["Date"].append(t)


    H_VaR, H_E_SF=hist_risk(window,alpha)
    di["H_VaR"].append(H_VaR)
    di["H_ES"].append(H_E_SF)
    if hist_percent_vec[t] <-H_VaR:
      di["H_breachoVaR"].append(1)
    else:
      di["H_breachoVaR"].append(0)

    N_VaR, N_E_SF=normal_riskp(alpha,window)
    di["N_VaR"].append(N_VaR)
    di["N_ES"].append(N_E_SF)
    if hist_percent_vec[t] <-N_VaR:
      di["N_breachoVaR"].append(1)
    else:
      di["N_breachoVaR"].append(0)

    t_VaR, t_E_SF=student_risk(alpha, window)
    di["T_VaR"].append(t_VaR)
    di["T_ES"].append(t_E_SF)
    if hist_percent_vec[t] <-t_VaR:
      di["T_breachoVaR"].append(1)
    else:
      di["T_breachoVaR"].append(0)



    G_VaR, G_E_SF, o_model=compute_garch_risk(o_model, alpha,window)
    di["G_VaR"].append(G_VaR)
    di["G_ES"].append(G_E_SF)
    if hist_percent_vec[t] <-G_VaR:
      di["G_breachoVaR"].append(1)
    else:
      di["G_breachoVaR"].append(0)

    if t%100==0:
      values = hist_percent_vec[t-BURNIN:t]
      total_D =len(di["H_breachoVaR"])
      #Historical
      H_ES=di["H_ES"][-1]
      ES_E_H.append(ES_error(values, H_ES))
      BR_H.append(sum(di["H_breachoVaR"])/total_D)

      #Normal
      N_ES=di["N_ES"][-1]
      ES_E_N.append(ES_error(values, N_ES))
      BR_N.append(sum(di["N_breachoVaR"])/total_D)
      #Student
      T_ES=di["T_ES"][-1]
      ES_E_T.append(ES_error(values, T_ES))
      BR_T.append(sum(di["T_breachoVaR"])/total_D)
      #GARCH
      G_ES=di["G_ES"][-1]
      ES_E_G.append(ES_error(values, G_ES))
      BR_G.append(sum(di["G_breachoVaR"])/total_D)

  return ES_E_H,ES_E_N,ES_E_T,ES_E_G,BR_H,BR_N,BR_T,BR_G
