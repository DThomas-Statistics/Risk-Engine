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

    N_VaR, N_E_SF=Normal_riskp(window,alpha)
    di["N_VaR"].append(N_VaR)
    di["N_ES"].append(N_E_SF)
    if hist_percent_vec[t] <-N_VaR:
      di["N_breachoVaR"].append(1)
    else:
      di["N_breachoVaR"].append(0)

    t_VaR, t_E_SF=student_risk(window,alpha)
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



