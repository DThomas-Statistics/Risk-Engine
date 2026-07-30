# Risk-Engine

##Project Overview

This project provides the framework to compute Value at Risk (VaR) and Expected Shortfall (ES) of a portfolio, enabling the user to conduct their own risk analysis. It includes three baseline models: Historical, Normal and Student-t as well as a dynamic volatility model selected through an AIC/BIC tournament to identify the optimal GARCH. 

In addition to computing these models, the project includes a backtesting function and statistical hypothesis tests such as Proportion of Failures (POF) and Christoffersen Independence Test (CIT) to evaluate the risk engine.


##About the Author

This project was developed as the start of my coding portfolio to assist me in job applications. I hold a BSc in Mathematics with Statistics for Finance (First) from the University of Bristol, and will progress to an MSc in Engineering Mathematics. Furthermore, I wanted this project to strengthen my ability in python as well as showcase my statistical ability on real-data.


## Features
* Compute Value at Risk (VaR) and Expected Shortfall (ES)
* Three baseline models: Historical, Normal and Student-t
* GARCH model selected via AIC and BIC
* Backtesting function for VaR/ES
* POF and CIT test for backtester validation
* Additional statistical tools: ACF, Kurtosis and Ljung-box test (WIP)

## Sources
This project draws heavily from **Financial Risk Forecasting** by Jon Danielsson for its simple foundation for financial forecasting and for further statistical and modelling understanding **Financial Econometrics** lecture notes by Kevin Sheppard. In addition to these primary sources, I have cited websites, documentation pages and forum discussions that provided guidance during development and were influential enough to be acknowledged.

## License
This project is licensed under the MIT License.

## Contributing
Contributions and suggestions are welcome.


## Roadmap
* Preparing a risk report of my own portfolio to demonstrate further understanding of statistical tests as well as show a broader range of analytical ability.
* Addition of Monte Carlo forecasting using baseline and dynamic models, this will enable simulation-based risk analysis for particular events that the user may cultivate and stress testing.


## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/DThomas-Statistics/Risk-Engine.git
cd Risk-Engine
pip install -r requirements.txt
