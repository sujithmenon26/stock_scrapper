import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
stocks1 = ["AAPL"]
stocks2 = ["SPY"]
data1 = yf.download(stocks1,  start='2018-01-01', end='2018-05-01')
data2 = yf.download(stocks2,  start='2018-01-01', end='2018-05-01')
data1.to_csv('aapl.csv')
data2.to_csv('syp.csv')
print(data1.head())
print(data2.head())
plt.plot(data1, color='red' ,label='Apple')
plt.plot(data2, color='blue',label='SYP')
plt.show()