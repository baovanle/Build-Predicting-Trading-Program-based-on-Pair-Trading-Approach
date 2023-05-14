#Ho: It is have unit root, non-stationary
#H1: It is stationary

def adfuller_test(price):
    result = adfuller(price)
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(label+' : '+str(value) )
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")
        
 adfuller_test(df['x1']).diff().dropna())
 adfuller_test(df['x2']).diff().dropna())
 adfuller_test(df['x3']).diff().dropna())
 adfuller_test(df['x4']).diff().dropna())
 adfuller_test(df['x5']).diff().dropna())

def find_cointegrated_pairs(data):
    n = data.shape[1]
    score_matrix = np.zeros((n, n))
    pvalue_matrix = np.ones((n, n))
    keys = data.keys()
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            S1 = data[keys[i]]
            S2 = data[keys[j]]
            result = coint(S1, S2)
            score = result[0]
            pvalue = result[1]
            score_matrix[i, j] = score
            pvalue_matrix[i, j] = pvalue
            if pvalue < 0.05:
                pairs.append((keys[i], keys[j]))
    return score_matrix, pvalue_matrix, pairs
  
  tickers= ['x1','x2','x3','x4']
  
  scores, pvalues, pairs = find_cointegrated_pairs(df[['x1','x2','x3','x4']])
import seaborn
fig, ax = plt.subplots(figsize=(10,10))
seaborn.heatmap(pvalues, xticklabels=tickers, yticklabels=tickers, cmap='RdYlGn_r' 
                , mask = (pvalues >= 0.05), annot=True
                )
print(pairs)
