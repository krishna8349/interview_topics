import pandas as pd

cols = ['loan_amnt', 'int_rate', 'installment']
data = pd.read_csv('loan.csv', nrows = 30000, usecols = cols)