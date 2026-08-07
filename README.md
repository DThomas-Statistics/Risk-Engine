> ⚠️ **Work in Progress**  
> This project is intentionally published early for employer review.  
> Some sections are incomplete and occasional errors may appear as development continues.

---



# Risk-Engine

## Project Overview

This project provides the framework to compute Value at Risk (VaR) and Expected Shortfall (ES) of a portfolio, enabling the user to conduct their own risk analysis. It includes three baseline models: Historical, Normal and Student-t as well as a dynamic volatility model selected through an AIC/BIC tournament to identify the optimal GARCH. 

In addition to computing these models, the project includes a backtesting function and statistical hypothesis tests such as Proportion of Failures (POF) and Christoffersen Independence Test (CIT) to evaluate the risk engine.

This project forms part of my quantitative coding portfolio and is intended to showcase my quantitative skills to employers.
## Features
* Compute Value at Risk (VaR) and Expected Shortfall (ES)
* Three baseline models: Historical, Normal and Student-t
* GARCH model selected via AIC and BIC
* Backtesting function for VaR/ES
* POF and CIT test for backtester validation
* Additional statistical tools: ACF, Kurtosis and Ljung-Box test (WIP)

## Installation
Clone the repository and install dependencies:

## Quick Start
This example backtest notebook is included because the engine does not include data-cleaning utilities. It provides the user with a demonstration of its intended use.
```bash
# Clone the repository
!git clone https://github.com/DThomas-Statistics/Risk-Engine.git

# Change directory
%cd Risk-Engine

# Install dependencies
!pip install -r requirements.txt

# Open notebooks/backtest_EXAMPLE.ipynb in your Jupyter or Colab environment
```
## Results Preview
Below is a graph illustrating how the models performed relative to the expected breach rate found in notebooks/backtest_EXAMPLE.ipynb. In addition, our dynamic GARCH model successfully passed the POF and CIT.
(This test is slightly rushed and will be updated in time as currently I am preparing for applications, THANK YOU.)
<img width="1242" height="684" alt="image" src="https://github.com/user-attachments/assets/13ad9161-86bf-4933-a0c4-4818026b3732" />


## Sources
This project draws heavily from **Financial Risk Forecasting** by Jon Danielsson for its simple foundation for financial forecasting and for further statistical and modelling understanding **Financial Econometrics** lecture notes by Kevin Sheppard. In addition to these primary sources, I have cited websites, documentation pages and forum discussions that provided guidance during development and were influential enough to be acknowledged.

## Contributing
Contributions and suggestions are welcome.

## About the Author

This project was developed as the start of my coding portfolio to assist me in job applications. I hold a BSc in Mathematics with Statistics for Finance (First) from the University of Bristol, and will progress to an MSc in Engineering Mathematics. Furthermore, I wanted this project to strengthen my ability in Python as well as showcase my statistical ability on real data.
## License
This project is licensed under the MIT License.

## Artificial Intelligence usage
This engine was developed manually without the use of AI-generated code. AI tools were used when combining all of my functions together and solely for debugging purposes. For example, when increasing the burn-in period AI assisted in identifying a bug where the ARCH package was using differing names for distributions causing an issue in compatibility between findGARCH and compute_garch_risk.

## Roadmap
* Preparing a risk report of my own portfolio to demonstrate further understanding of statistical tests as well as show a broader range of analytical ability.
* Addition of Monte Carlo forecasting using baseline and dynamic models, this will enable simulation-based risk analysis for particular events that the user may cultivate and stress testing.
